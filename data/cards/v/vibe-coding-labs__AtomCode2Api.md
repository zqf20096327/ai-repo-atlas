# vibe-coding-labs/AtomCode2Api

⭐ 15 · Go · Apache-2.0 · 推送 2026-08-03 · [GitHub](https://github.com/vibe-coding-labs/AtomCode2Api) · [官网](https://github.com/vibe-coding-labs/AtomCodeProxy) · 组织维护 · 中文 README

**把 AtomCode 免费额度转成 OpenAI/Anthropic 标准接口的代理**

Go 编写的反向代理服务：读取本地运行的 AtomCode（CodingPlan Lite）Daemon 的私有协议，将其翻译为 OpenAI 与 Anthropic 标准接口，使 Claude Code、Codex、Cursor 等只认标准接口的工具可以直接消耗 AtomCode 的免费模型额度（如 deepseek-v4-flash、Qwen3-VL-8B）。自带 Web 管理面板（端口 45678），提供账号管理、用量图表、请求日志与启动命令一键复制。运行前提是 AtomCode 已登录并在后台运行；支持源码编译与 Docker 两种部署方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将 AtomCode 私有协议翻译为 OpenAI/Anthropic 标准接口
- Web 管理面板：账号导入、数据概览、请求日志、套餐信息
- 提供 Claude Code / Codex / Cursor 的配置命令一键复制
- Go 实现，支持源码编译与 Docker 两种运行方式

## 适用场景

- 让 Claude Code / Codex / Cursor 使用 AtomCode 免费额度写代码
- 在 Web 面板统一管理 AtomCode 账号与查看调用日志
- 免购买 OpenAI API Key 搭建本地标准接口端点

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L21: 简单说就是：**AtomCode 有个免费版（CodingPlan Lite），每个月能免费用很多次 AI。但 Claude Code、Cursor、Codex 这些工具连不上它，因为 AtomCode 用的是自己的私有协议，不是
> L23: AtomCode2API 就是一个"翻译官"——它坐在你的工具和 AtomCode 之间，把工具发的标准请求翻译成 AtomCode 能听懂的话，再把 AtomCode 的回复翻译回来。
> L48: 你有 AtomCode 的免费额度，但你想用 Claude Code 或者 Codex 或者 Cursor 来写代码。这些工具只认 OpenAI 和 Anthropic 的标准接口，不认 AtomCode 的私有协议。

## 星数曲线

```mermaid
xychart-beta
    title "vibe-coding-labs/AtomCode2Api 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a7e95c99179e` · [字段定义](../../DATASET.md)*
