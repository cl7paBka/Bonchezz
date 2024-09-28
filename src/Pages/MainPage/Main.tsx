import './Main.scss'
import {l} from "vite/dist/node/types.d-aGj9QkWt";

function Main() {
    return(
    <>
    <div className="header inter-text">
        <div className="logo">
            <img src={""} alt={"Лого"}/>
            <h3>Название</h3>
        </div>
        <div className={"profile"}>
            <p>Александр Тетерин</p>
            <img src={""} alt={"Фото"}/>
        </div>
    </div>
    <div className="body inter-text">
        <div className={"sidebar"}>
            <div className={"tabButton"}>
                <i className="material-icons">home</i>
                <div className={"tabText"}>Обзор</div>
            </div>
            <div className={"tabButton"}>
                <i className="material-icons">content_copy</i>
                <div className={"tabText"}>Проекты</div>
            </div>
            <div className={"tabButton"}>
                <i className="material-icons">checklist</i>
                <div className={"tabText"}>Задачи</div>
            </div>
            <div className={"line"}/>
            <div className={"tabButton"}>
                <i className="material-icons">add_box</i>
                <div className={"tabText"}>Проекты</div>
            </div>
        </div>
        <div className={"menu inter-text"}>
            <h5>Обзор</h5>
            <h3>Добрый вечер, Александр!</h3>
            <h5>Суббота, 28 сентября 2024</h5>
            <div className={"line"}></div>
            <p>Важные проекты</p>
            <div className={"line"}></div>
            <div className={"activity"}>
                <div className={"projectForm"}>
                    Задача 1
                </div>
                <div className={"projectForm"}>
                    осталось дней: 1
                </div>
            </div>
            <div className={"activity"}>
                <div className={"projectForm"}>
                    Задача 2
                </div>
                <div className={"projectForm"}>
                    осталось дней: 4
                </div>
            </div>
        </div>
    </div>
    </>
    )
}

export default Main