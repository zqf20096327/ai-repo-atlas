# ob-labs/memory-powermem

⭐ 30 · TypeScript · Apache-2.0 · 推送 2026-05-21 · [GitHub](https://github.com/ob-labs/memory-powermem) · 组织维护 · 中文 README

**为 OpenClaw bot 接入 PowerMem 长期记忆的插件**

OpenClaw 插件，将 PowerMem 长期记忆系统接入 OpenClaw agent：提供智能抽取、艾宾浩斯遗忘曲线回忆、多用户/多 agent 隔离，支持对话结束后自动存储（autoCapture）、会话开始前自动注入相关记忆（autoRecall）、LLM 提取过程性经验。后端支持 CLI 模式（本地 pmem + SQLite）与 HTTP 模式（连接共享 PowerMem API，支持 v2 请求级配置与双写）。默认 CLI 模式，npm 安装，面向 OpenClaw 个人与团队用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 智能抽取 + 艾宾浩斯遗忘曲线 + 多 agent 隔离的长期记忆
- CLI（本地 SQLite）与 HTTP（共享服务器）双模式
- autoCapture/autoRecall/autoExperience 默认开启
- 可一次性导入 OpenClaw 现有 markdown 记忆

## 适用场景

- 让我的 OpenClaw bot 跨会话记住偏好与事实
- 多用户/多 agent 环境下隔离共享记忆
- 把已有的 markdown 记忆文件迁移到 PowerMem

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: # OpenClaw Memory (PowerMem) Plugin
> L7: This plugin lets OpenClaw use long-term memory via PowerMem: intelligent extraction, Ebbinghaus forgetting curve, mu

## 星数曲线

```mermaid
xychart-beta
    title "ob-labs/memory-powermem 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-31 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `906a5a50c670` · [字段定义](../../DATASET.md)*
