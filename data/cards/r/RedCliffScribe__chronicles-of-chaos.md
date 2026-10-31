# RedCliffScribe/chronicles-of-chaos

⭐ 14 · TypeScript · AGPL-3.0 · 推送 2026-08-17 · [GitHub](https://github.com/RedCliffScribe/chronicles-of-chaos) · 个人维护 · 中文 README

**LLM 驱动的三国乱世本地互动叙事 RPG**

由大语言模型驱动叙事与推演的三国互动 RPG：玩家自创角色或扮演史实人物进入东汉末年，本地运行时负责结构化写回校验、人物记忆管理（近期+压缩中长期）、势力/领地/部队演化与确定性战斗结算，LLM 仅负责理解行动与生成叙事。存档默认存于浏览器 IndexedDB，模型请求由浏览器直连玩家自选第三方服务。React/TypeScript 项目，需 Node.js 环境下 npm 构建运行；内置十余家 API 配置入口并支持 OpenAI-compatible 与 Ollama/LM Studio 本地后端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 叙事 + 本地结构化写回：正文不能绕过事实层改写世界状态
- NPC 具备记忆压缩与离屏自主行动；势力、领地、部队随游戏时间演化
- 可拆分模型路由：主剧情、写回、记忆压缩、嵌入等可分别配置 API 与模型
- 本地优先数据链：IndexedDB 存档、导入导出、回合回溯，可选 Cloudflare 云存档

## 适用场景

- 扮演三国人物或自创角色体验不重置的持续世界线
- 接入自己选择或本地部署的 LLM 服务进行长存档叙事
- 在桌面与移动端之间同步云存档继续游玩

## 场景标签

 · 领域:游戏/互动叙事

## 证据(README 行号)

> L5: 一款由大语言模型驱动、让人物与天下局势在本地结构化状态中持续演化的三国乱世互动叙事 RPG。
> L64: 项目内置 OpenAI、DeepSeek、Gemini、Anthropic Claude、Qwen、智谱 GLM（含 Coding Plan）、MiniMax、Moonshot/Kimi、豆包、xAI、Groq、Mistral、O

## 星数曲线

```mermaid
xychart-beta
    title "RedCliffScribe/chronicles-of-chaos 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `ca8a92dc9188` · [字段定义](../../DATASET.md)*
