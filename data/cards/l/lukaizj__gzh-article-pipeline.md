# lukaizj/gzh-article-pipeline

⭐ 21 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/lukaizj/gzh-article-pipeline) · 个人维护 · 中文 README

**面向公众号运营者的 AI 创作发布闭环 Skill 流水线**

以 Codex / Claude Code / Antigravity Skill 形式安装的微信公众号内容流水线，覆盖选题核验、标题评分、21:9 封面生成、短段排版、9 项离线质检、草稿直推公众号后台与免密钥后台数据复盘。作者称基于近 180 篇实操数据沉淀规则（eCPM 选品、三道递进闸门）。本地 Python 运行，推草稿需 appid/appsecret，网页接管与复盘需 macOS + Chrome。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双高选题与标题四维打分门禁（<75 分打回）
- 21:9 剧情封面生成，API 429 限流时接管本机 Chrome Gemini 网页版出图
- 9 项离线质检脚本 validate_article.py 零密钥运行
- 免 appid/appsecret 复用本机 Chrome 登录态拉取完读率与推荐流数据

## 适用场景

- 让 AI 助手按 URL 一步完成验活、写稿、配图、质检并推草稿箱
- 发布前离线扫描文章套话、违禁词与内联结构
- 免密钥拉取后台完读率反哺下期选题

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L14:  从选题、剧情封面、千字短段排版到草稿直推与后台复盘的公众号 Skill 流水线
> L15:  基于「奇点造物所」近 180 篇实操数据打磨，支持 Codex / Antigravity / Claude Code 直接调用。
> L31: - **双高选题 & 标题门禁**：核查项目近况防推僵尸仓，按高 eCPM 赛道选品；标题 `<= 26` 字四维打分（`< 75` 分打回），剔除劝退黑话。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `e1a19aac8f27` · [字段定义](../../DATASET.md)*
