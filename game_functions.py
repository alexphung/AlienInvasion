"""
    This module will hold all the game functions.
"""
import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien
from sound import AiSound
from explosion import Explosion

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,
        bullets):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button,  
                ship, aliens, bullets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN : 
            check_keydown_events(event, ai_settings, screen, stats, sb,
                ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
def check_play_button(ai_settings, screen, stats, sb, play_button, ship, 
        aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True
        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # Load Background Game Music
        pygame.mixer.music.load('game_sounds/music_background.wav')
        # Start background music.
        pygame.mixer.music.play(-1, 0.0)

def check_keydown_events(event, ai_settings, screen, stats, sb, ship, 
        aliens, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        # Move the ship to the right    
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        # Move the ship to the left    
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if stats.game_active and not stats.game_pause:
            fire_bullet(ai_settings, screen, ship, bullets)
            # Add shooting sound effect
            shot_sound = AiSound()
            shot_sound.play_blasting()
    elif event.key == pygame.K_p:
        stats.game_pause = True
        pygame.mixer.music.pause()
    elif event.key == pygame.K_r:        
        stats.game_pause = False
        pygame.mixer.music.unpause()
    elif event.key == pygame.K_n:
        start_new_game(ai_settings, screen, stats, sb, ship, aliens, bullets)        
        pygame.mixer.music.unpause()
    elif event.key == pygame.K_q:
        sys.exit()
            
def start_new_game(ai_settings, screen, stats, sb, ship, aliens, bullets):
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        # Reset the game statistics.
        stats.reset_stats()
        stats.game_won = False
        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        
def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Respond to key releases."""    
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        # Stop the ship from moving right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        # Stop the ship from moving left
        ship.moving_left = False

def update_screen(ai_settings, screen, stats, sb, ship, aliens, 
        bullets, play_button, explosion_sprites):
    """Update images on the screen and flip to the new screen.""" 
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()  
    ship.blitme()
    aliens.draw(screen)
    
    # Draw the score information.
    sb.show_score()
    
    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()
            
    # Draw the explosion sprites
    explosion_sprites.draw(screen)  
    
    # Make the most recently draw screen visible.
    pygame.display.flip()
    
def update_bullets(ai_settings, screen, stats, sb, ship, aliens, 
        bullets, explosion_anim, explosion_sprites):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()
            
    # Get rid of old bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,
        aliens, bullets, explosion_anim, explosion_sprites)
            
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, 
        aliens, bullets, explosion_anim, explosion_sprites):
    """Respond to bullet-alien collisions."""
    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the aliens.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            for alien in aliens:
                # Explosion sound effect.
                explode = AiSound()
                explode.play_enemy_exploding()     
                expl = Explosion(explosion_anim, alien.rect.center, 'lg')
                explosion_sprites.add(expl)                                           
                if alien.id == 3:
                    stats.score += (ai_settings.alien_points * 3 * ai_settings.score_scale)
                    stats.purple_alien_destroyed += 1
                    print("Hit:\t" + 
                            str(ai_settings.alien_points * 3 * ai_settings.score_scale))
                    print("Purple Alien Killed: " + 
                            str(stats.purple_alien_destroyed))      
                elif alien.id == 2:
                    stats.score += (ai_settings.alien_points * 2 * ai_settings.score_scale)
                    stats.red_alien_destroyed += 1
                    print("Hit:\t" + 
                            str(ai_settings.alien_points * 2 * ai_settings.score_scale))
                    print("Red Alien Killed: " + 
                            str(stats.red_alien_destroyed))
                else:                    
                    stats.score += ai_settings.alien_points
                    stats.green_alien_destroyed += 1
                    print("Hit:\t" + 
                            str(ai_settings.alien_points))
                    print("Green Alien Killed: " + 
                            str(stats.green_alien_destroyed))
            sb.prep_score()
            check_upgrade_weapon(ai_settings, stats)
        check_high_score(stats, sb)
    if len(aliens) == 0:
        # Destroy existing bullets and create new fleet.
        bullets.empty()   
        # Increase Level.
        if stats.level < stats.game_max_level:
            stats.level += 1
        else:
            stats.game_won = True
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)

def check_upgrade_weapon(ai_settings, stats):
    """Upgrade the bullet settings according to the aliens killed stats."""
    if stats.green_alien_destroyed == 50:
        ai_settings.increase_bullet_size()
        stats.green_alien_destroyed = 0
        
    if stats.red_alien_destroyed == 50:
        ai_settings.increase_bullets_allowed()
        stats.red_alien_destroyed = 0
    
    if stats.purple_alien_destroyed == 50:
        ai_settings.upgrade_weapon((0, 0, 233))
        stats.purple_alien_destroyed = 0
        
def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    # Spacing between each alien is equal to one alien width.
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
    
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""    
    # Create an alien and place it in the row.
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens taht fit on the screen."""
    available_space_y = (ai_settings.screen_height -
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows    
    
def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height)
        
    # Create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                row_number)
        
def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    
def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    # Set game_active to False if the player has used up all their ships.
    if stats.ships_left > 0:
        # Decrement ships_left.
        stats.ships_left -= 1
        # Update scoreboard
        sb.prep_ships()
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # Pause.
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        # Stop background music
        pygame.mixer.music.stop()
    
def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            print("Aliens landed!!!")
            break
    
def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    Check if the fleet is at an edge,
      and then update teh positions of all the aliens in the fleet.
    """
    check_fleet_edges(ai_settings, aliens)
    """Update the positions of all aliens in the fleet."""
    aliens.update()
    
    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
        print("Ship hit!!!")
    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)
    
def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
        
