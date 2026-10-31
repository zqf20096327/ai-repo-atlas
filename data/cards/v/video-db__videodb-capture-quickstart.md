# video-db/videodb-capture-quickstart

⭐ 29 · Python · ISC · 推送 2026-08-12 · [GitHub](https://github.com/video-db/videodb-capture-quickstart) · [官网](https://docs.videodb.io/pages/ingest/capture-sdks/overview) · 组织维护

**给 AI agent 提供实时桌面感知的屏幕/音频采集 SDK**

VideoDB Capture SDK 提供桌面屏幕、麦克风与系统音频的实时采集与流式传输：后端创建会话并铸造短期 token（API key 留在服务端），桌面客户端用 token 推流，VideoDB Cloud 执行 AI 处理（转录、视觉/音频索引），经 webhook 与 WebSocket 交付结构化事件（转写文本、场景描述、语义索引），延迟低于 2 秒。提供 npm 与 pip 安装，需注册 console.videodb.io 获取 API key；另附 6 个示例应用与 Node.js/Python 快速开始代码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | ISC |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 采集屏幕、麦克风、系统音频并实时流式传输
- 后端铸造短期 token，客户端不接触 API key
- webhook + WebSocket 交付带时间戳的结构化事件（转录/场景索引/音频索引）
- 提供 6 个可本地运行的示例应用（Pair Programmer、Call.md 等）

## 适用场景

- 让编码 agent 获得屏幕与语音的实时上下文
- 构建实时会议转录与纪要应用
- 全天屏幕记录并用自然语言查询历史内容

## 场景标签

`语音识别` `多模态` · 领域:感知与多模态

## 证据(README 行号)

> L29: VideoDB Capture gives AI agents eyes and ears—stream screen, mic, and system audio for real-time processing, delive
> L34: - VideoDB Cloud runs AI processing and delivers events via webhooks + WebSocket

## 星数曲线

```mermaid
xychart-beta
    title "video-db/videodb-capture-quickstart 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-31 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a5a43d22c914` · [字段定义](../../DATASET.md)*
