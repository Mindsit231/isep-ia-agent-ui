import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';


interface Chat {
  id: string;
  title: string;
  timestamp: Date;
}
@Component({
  selector: 'app-accueil',
  imports: [FormsModule],
  templateUrl: './accueil.html',
  styleUrl: './accueil.scss'
})
export class Accueil {
  message: string = '';
  recentChats: Chat[] = [];
  isSidebarOpen: boolean = false;

  suggestions = [
    { text: 'Explain a complex concept', icon: '💡' },
    { text: 'Help me write something', icon: '✍️' },
    { text: 'Brainstorm ideas', icon: '🧠' },
    { text: 'Answer my questions', icon: '❓' }
  ];

  toggleSidebar(): void {
    this.isSidebarOpen = !this.isSidebarOpen;
  }

  newConversation(): void {
    console.log('Starting new conversation');
    this.message = '';
  }

  sendMessage(): void {
    if (this.message.trim()) {
      console.log('Sending message:', this.message);
      // Logique d'envoi du message
      this.message = '';
    }
  }

  selectSuggestion(suggestion: string): void {
    this.message = suggestion;
  }

  onKeyPress(event: KeyboardEvent): void {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      this.sendMessage();
    }
  }
}


