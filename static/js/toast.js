function showToast(title, message, type = 'normal', duration = 3500) {
    const toast = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    const toastIcon = document.getElementById('toast-icon');
    
    if (!toast) return;

    // Reset semua gaya dulu
    toast.style.backgroundColor = '#f9f9f9ff';
    toast.style.border = '4px solid #B39A84';
    toast.style.color = '#0A1E54';
    toastIcon.textContent = '';
    
    // Tentukan warna dan ikon berdasarkan tipe
    let icon = '💬'; // default icon
    let bg = '#F9F0EE';
    let border = '#B39A84';
    let text = '#0A1E54';
    
    if (type === 'success') {
        icon = '✅';
        bg = '#E8F5E9';      // soft green background
        border = '#A5D6A7';  // gentle green border
        text = '#1B5E20';    // dark green text
    } else if (type === 'error') {
        icon = '❌';
        bg = '#FDECEA';      // soft red background
        border = '#F5C6CB';  // gentle red border
        text = '#7F1D1D';    // dark red text
    } else if (type === 'info') {
        icon = 'ℹ️';
        bg = '#E3F2FD';      // soft blue background
        border = '#90CAF9';  // gentle blue border
        text = '#0A1E54';    // main blue
    } else if (type === 'warning') {
        icon = '⚠️';
        bg = '#FFF8E1';      // soft yellow background
        border = '#FFE082';  // gentle yellow border
        text = '#8D6E63';    // warm brown text
    }

    // Apply style
    toast.style.backgroundColor = bg;
    toast.style.border = `2px solid ${border}`;
    toast.style.color = text;

    // Isi teks
    toastIcon.textContent = icon;
    toastTitle.textContent = title;
    toastMessage.textContent = message;

    // Animasi muncul
    toast.classList.remove('opacity-0', 'translate-y-64');
    toast.classList.add('opacity-100', 'translate-y-0');

    // Auto-hide dengan efek fade
    clearTimeout(toast.hideTimeout);
    toast.hideTimeout = setTimeout(() => {
        toast.classList.remove('opacity-100', 'translate-y-0');
        toast.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}

// Contoh pemakaian:
// showToast('Login Successful', 'Welcome back!', 'success');
// showToast('Item Deleted', 'Your product was removed.', 'error');
// showToast('Welcome!', 'Thanks for registering.', 'info');
