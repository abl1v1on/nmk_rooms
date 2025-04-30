export default function MainPage() {
    return (
        <>
        <section className="hero is-medium is-dark">
          <div className="hero-body">
              <div className="container has-text-centered">
                  <h1 className="title is-2 has-text-weight-bold mb-4">Конференц-залы</h1>
                  <p className="subtitle is-4">Бронирование залов для встреч и мероприятий</p>
              </div>
          </div>
        </section>

        <section className="section pt-5 pb-2">
          <div className="container">
              <div className="box">
                  <div className="columns is-vcentered">
                      <div className="column is-4">
                          <div className="field">
                              <div className="control has-icons-left">
                                  <input className="input" type="text" placeholder="Поиск по названию..." />
                                  <span className="icon is-small is-left">
                                      <i className="fas fa-search"></i>
                                  </span>
                              </div>
                          </div>
                      </div>
                      <div className="column is-3">
                          <div className="field">
                              <div className="control">
                                  <div className="select is-fullwidth">
                                      <select>
                                          <option>Все корпуса</option>
                                          <option>Корпус А</option>
                                          <option>Корпус Б</option>
                                          <option>Корпус В</option>
                                      </select>
                                  </div>
                              </div>
                          </div>
                      </div>
                      <div className="column is-3">
                          <div className="field">
                              <div className="control">
                                  <div className="select is-fullwidth">
                                      <select>
                                          <option>Любая вместимость</option>
                                          <option>До 10 человек</option>
                                          <option>10-20 человек</option>
                                          <option>20+ человек</option>
                                      </select>
                                  </div>
                              </div>
                          </div>
                      </div>
                      <div className="column is-2">
                          <button className="button is-black is-fullwidth">
                              <span className="icon">
                                  <i className="fas fa-filter"></i>
                              </span>
                              <span>Применить</span>
                          </button>
                      </div>
                  </div>
              </div>
          </div>
        </section>

        <section className="section pt-2">
          <div className="container">
              <div className="columns is-multiline">
                  <div className="column is-one-third">
                      <div className="card hall-card">
                          <div className="card-image">
                              <figure className="image is-4by3">
                                  <img src="" alt="Зал 'Нефтяник'" />
                              </figure>
                          </div>
                          <div className="card-content">
                              <div className="media">
                                  <div className="media-content">
                                      <p className="title is-4">Нефтяник</p>
                                      <p className="subtitle is-6">Корпус А, 3 этаж</p>
                                  </div>
                                  <div className="media-right">
                                      <span className="tag is-primary">20 чел.</span>
                                  </div>
                              </div>

                              <div className="content">
                                  <p>Современный зал с проектором и звуковой системой. Идеально для презентаций.</p>
                                  <div className="buttons mt-4">
                                      <a href="" className="button is-black is-outlined is-fullwidth">
                                          <span>Подробнее</span>
                                          <span className="icon">
                                              <i className="fas fa-arrow-right"></i>
                                          </span>
                                      </a>
                                  </div>
                              </div>
                          </div>
                      </div>
                  </div>

                  <div className="column is-one-third">
                      <div className="card hall-card">
                          <div className="card-image">
                              <figure className="image is-4by3">
                                  <img src="" alt="Зал 'Сибирский'" />
                              </figure>
                          </div>
                          <div className="card-content">
                              <div className="media">
                                  <div className="media-content">
                                      <p className="title is-4">Сибирский</p>
                                      <p className="subtitle is-6">Корпус Б, 1 этаж</p>
                                  </div>
                                  <div className="media-right">
                                      <span className="tag is-primary">12 чел.</span>
                                  </div>
                              </div>

                              <div className="content">
                                  <p>Уютный зал для небольших совещаний с маркерной доской.</p>
                                  <div className="buttons mt-4">
                                      <a href="" className="button is-black is-outlined is-fullwidth">
                                          <span>Подробнее</span>
                                          <span className="icon">
                                              <i className="fas fa-arrow-right"></i>
                                          </span>
                                      </a>
                                  </div>
                              </div>
                          </div>
                      </div>
                  </div>

                  <div className="column is-one-third">
                      <div className="card hall-card">
                          <div className="card-image">
                              <figure className="image is-4by3">
                                  <img src="" alt="Зал 'Урал'" />
                              </figure>
                          </div>
                          <div className="card-content">
                              <div className="media">
                                  <div className="media-content">
                                      <p className="title is-4">Урал</p>
                                      <p className="subtitle is-6">Корпус В, 2 этаж</p>
                                  </div>
                                  <div className="media-right">
                                      <span className="tag is-primary">30 чел.</span>
                                  </div>
                              </div>

                              <div className="content">
                                  <p>Большой конференц-зал с видео-конференц связью и круглым столом.</p>
                                  <div className="buttons mt-4">
                                      <a href="" className="button is-black is-outlined is-fullwidth">
                                          <span>Подробнее</span>
                                          <span className="icon">
                                              <i className="fas fa-arrow-right"></i>
                                          </span>
                                      </a>
                                  </div>
                              </div>
                          </div>
                      </div>
                  </div>
              </div>
          </div>
        </section>
      </>
    )
}