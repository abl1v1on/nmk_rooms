export default function SingleBooking({ booking, handleDeleteBooking }) {
    const getBookingStatus = () => {
        const bookingDate = new Date(booking.booking_date).setHours(0, 0, 0, 0);
        const currentDate = new Date().setHours(0, 0, 0, 0);

        if (bookingDate < currentDate) {
            return "Завершено";
        }
        return "Подтверждено"
    };
    
    return (
        <div className="booking-card">
            <div className="booking-card-header">
                <div className="columns is-vcentered is-mobile">
                    <div className="column">
                        <h3 className="title is-4 mb-0">Конференц-зал №{booking.room.number}</h3>
                        <span className="booking-status status-confirmed mt-3">
                            <span className="icon is-small">
                                <i className={`fas fa-${getBookingStatus() === "Завершено" ? "history" : "check-circle"} mr-2`}></i>
                            </span>
                            <span>{getBookingStatus()}</span>
                        </span>
                    </div>
                    <div className="column is-narrow">
                        <button onClick={() => handleDeleteBooking(booking.id)} className="button is-light is-danger cancel-btn">
                            <span className="icon">
                                <i className="fas fa-times"></i>
                            </span>
                            <span>Отменить</span>
                        </button>
                    </div>
                </div>
            </div>
            <div className="booking-card-body">
                <div className="booking-details">
                    <div className="booking-detail">
                        <div className="detail-label">Дата и время</div>
                        <div className="detail-value">{booking.booking_date}, {booking.booking_time}</div>
                    </div>
                    <div className="booking-detail">
                        <div className="detail-label">Местоположение</div>
                        <div className="detail-value">{booking.room.location.address}</div>
                    </div>
                    <div className="booking-detail">
                        <div className="detail-label">Цель</div>
                        <div className="detail-value">{booking.goal ? booking.goal : "-"}</div>
                    </div>
                </div>
            </div>
        </div>
    )
}
