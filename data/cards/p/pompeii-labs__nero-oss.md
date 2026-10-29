# pompeii-labs/nero-oss

⭐ 43 · TypeScript · MIT · 推送 2026-07-27 · [GitHub](https://github.com/pompeii-labs/nero-oss) · [官网](https://nero.pompeiilabs.com) · 组织维护

**自托管单用户 AI 伴侣：语音/文本对话并代为执行任务**

运行在用户自有硬件上的单用户 AI agent 应用：以 Docker 四容器加主机侧 runner 组成小型栈，通过网页、手机 PWA 与语音访问同一 agent、记忆与会话。能力包括实时语音（Deepgram STT + LLM + ElevenLabs TTS 级联管线）、后台代码项目（子 agent、git worktree、开 PR）、知识图谱记忆、MCP 工具接入与投屏面板。持久化由单一 Lux 引擎承担，CLI 负责生成 compose 与生命周期管理，本地 HTTPS + mDNS 支持局域网语音。唯一主机依赖是 Docker，模型经 OPENROUTER_API_KEY 接入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四容器 + 主机 runner 的自托管栈，唯一主机依赖为 Docker
- 实时语音级联管线（Deepgram STT / LLM / ElevenLabs TTS，WebRTC sidecar）
- 后台项目：规划、子 agent、git worktree 中写码测试并开 PR
- 单一 Lux 引擎承担表/KV/向量/实时/队列/认证，备份即打包卷

## 适用场景

- 在家用服务器上跑一个跨设备共享记忆的私人 AI 助手
- 让 agent 在后台执行多步代码项目并提交 PR
- 通过 MCP 接入自有工具，用语音或文本唤起同一个 agent

## 场景标签

`AI 助手` `语音 Agent` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L12: Nero is a single-user AI companion you run yourself. No account, no cloud tenant, no
> L17: It is closer to Jarvis than to a chatbot: something that is *around*, that you talk to

## 星数曲线

```mermaid
xychart-beta
    title "pompeii-labs/nero-oss 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-29 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fb8eb45021ff` · [字段定义](../../DATASET.md)*
