// import './LoginPage.scss'
// import '../../main.tsx'
//
// function LoginPage() {
//     return(
//         <>
//             <div className='body'>
//                 <div className='container'>
//                     <h1 className='inter-text'>Рады вас видеть!</h1>
//                     <h4 className='inter-text' id='loginWarning'>Войдите, чтобы продолжить</h4>
//                     <label className={'inter-text'}>E-mail</label>
//                     <input className='inter-text' id='loginEmail' type='email' name='loginEmail' placeholder='example@example.com' />
//                     <label className='inter-text'>Пароль</label>
//                     <input  id='loginPassword' type='password' name='loginPassword' />
//                     <div id='rememberMe'>
//                         <div className='left-side'>
//                             <input className='rememberElements' id='rememberCheckbox' type='checkbox'
//                                    name='rememberCheckbox'/>
//                             <label className='rememberElements inter-text'>Запомнить меня</label>
//                         </div>
//                         <button className='rememberElements inter-text'>Забыли пароль?</button>
//                     </div>
//                     <div>
//                         <a href='../MainPage/Main.tsx'>
//                             <button className={'inter-text'}>Войти</button>
//                         </a>
//                     </div>
//                 </div>
//             </div>
//         </>
//     )
// }
//
// export default LoginPage;

import './LoginPage.scss';
import '../../main.tsx';

function LoginPage() {

    const handleGitlabLogin = () => {
        // Replace with your actual GitLab OAuth URL
        const gitlabOauthUrl = 'https://gitlab.com/oauth/authorize?client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URI&response_type=code&scope=read_user';
        window.location.href = gitlabOauthUrl;
    }

    return (
        <>
            <div className="body">
                <div className="container">
                    <h2 className="inter-text">Добро пожаловать!</h2>
                    <h6 className="inter-text" id="loginWarning">Войдите через GitLab, чтобы продолжить</h6>

                    {/* GitLab Login Button */}
                    <div>
                        <button className="inter-text" id="gitlabLoginButton" onClick={handleGitlabLogin}>
                            Войти через GitLab
                        </button>
                    </div>
                </div>
            </div>
        </>
    );
}

export default LoginPage;
