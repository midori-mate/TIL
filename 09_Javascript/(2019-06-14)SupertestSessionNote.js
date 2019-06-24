/**
 * SupertestSessionNote
 * 
 * $ npm install mocha supertest supertest-session --save-dev
 * 
 * マジでむずい
 * 
 * 
 */

const assert = require('assert');
const session = require('supertest-session');


/**
 * ログインがあるときの構成
 * 課題: ログインは before じゃなくて beforeEach とかでやりたいんだが、 beforeEach には async,await の処理を書きたい。
 * ほんで return done と async は共存させられねーんだよおおお!
 */
describe('', () => {

  let testSession;
  let authenticatedSession;

  before((done) => {
    testSession = session(sails.hooks.http.app);  // sails じゃないときどう書くのかはわからん……
    testSession.post('/login')
      .send({
        loginId : '...',
        password: '...',
      })
      .end((err) => {
        if (err) {
          return done(err);
        }
        authenticatedSession = testSession;
        return done();
      });
  });

  after(() => {
    testSession = undefined;
    authenticatedSession = undefined;
  });

  it('ログインが必要なテスト', (done) => {
    authenticatedSession.post('/api/...')
      .send({
        var: '',
      })
      .expect(200, {id:5}, done);
  });

});


/**
 * ただ API の返却をテストできればいいとき
 */
it('', (done) => {
  authenticatedSession.post('...')
    .send({
      var: '',
    })
    .expect(200, {
      id:5,
    }, done);
});


/**
 * API の返却だけじゃテストできんとき(返却以外に DB の中身を見ないといけないとか)
 * done を使わず return しないといけない注意。
 */
it('', () => {
  return authenticatedSession.post('...')
    .send({
      var: '',
    })
    .expect(200)
    .then((res) => {
      assert.deepEqual(res.body.id, 5);
    });
});


/**
 * then の中で await を使うとき
 * ちょっとドキドキしたけれど普通に async await つけて通る!
 */
it('', () => {
  return authenticatedSession.post('...')
    .send({
      var: '',
    })
    .expect(200)
    .then(async (res) => {
      await なんちゃら
    });
});


/**
 *
 */


