# chengyuZou/EmaAgent-Python-Prototype

⭐ 24 · Python · 推送 2026-04-23 · [GitHub](https://github.com/chengyuZou/EmaAgent-Python-Prototype) · [官网](https://www.bilibili.com/video/BV19WZgBfEJ9/?spm_id_from=333.1387.0.0) · 个人维护 · 中文 README

**面向 Live2D 角色的多模式 AI 智能体应用（对话/工具/剧情RAG）**

基于《魔法少女的魔女审判》角色艾玛构建的 Web 智能体应用，Python FastAPI 后端 + React 前端。提供 chat 普通对话、agent 工具调用（ReAct）、narrative 剧情检索（Router + LightRAG 多周目实例）三种模式，附带流式 TTS、会话持久化压缩、ChunkRAG 记忆、Live2D 状态联动、MCP 工具（高德导航/Howtocook）以及音乐播放、拼图游戏、资讯爬取等页面。LLM 接入 DeepSeek/Qwen/OpenAI 三选一，Embedding 与 TTS 使用 siliconflow。宣称替换人设 Prompt、Live2D 与参考音频即可扩展为其他角色。目前仅测试 Windows，主语言拟更换为 TypeScript。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- chat / agent(ReAct) / narrative(Router+LightRAG) 三模式智能体
- WebSocket 流式输出 + 分段 TTS + 会话压缩与 ChunkRAG 记忆
- MCP 工具集成（高德导航、Howtocook）与配置热重载
- 剧情数据清洗管线（Parser）与多周目 LightRAG 路由检索

## 适用场景

- 与 Live2D 角色艾玛进行对话、剧情问答与语音交互
- 替换人设与素材扩展成其他角色的智能体
- 作为个人 Agent 项目学习 ReAct、RAG 与 MCP 集成实现

## 场景标签

`聊天机器人` `RAG` `语音合成` · 领域:对话与助手

## 证据(README 行号)

> L19: EmaAgent 是一个多模式智能助手系统，也是我的第一个智能体项目。当前版本核心包含：
> L21: - `chat` 普通对话模式
> L23: - `narrative` 叙事检索模式（Router + LightRAG），支持不含 BE 的全剧情检索

## 星数曲线

```mermaid
xychart-beta
    title "chengyuZou/EmaAgent-Python-Prototype 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f6ab1357f5a0` · [字段定义](../../DATASET.md)*
