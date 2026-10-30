# kowais915/localbrain

⭐ 19 · TypeScript · NOASSERTION · 推送 2026-07-25 · [GitHub](https://github.com/kowais915/localbrain) · 个人维护

**一行命令在本地跑起 OpenAI 兼容端点，替应用省掉付费 API**

面向开发者的本地 AI 接入工具：npx localbrain 检测机器与项目环境，自动挑选并下载与硬件匹配的开源小模型（SmolLM2 / Qwen2.5，90MB–4.5GB），经 node-llama-cpp 推理在本机 4141 端口提供 OpenAI 兼容端点，并改写代码把付费 API 调用替换为本地端点（diff 可撤销）。配套零依赖的 JS 客户端库与 Rust crate。README 明确声明不适用于服务器托管场景与深度推理任务，仅限 Apache-2.0/MIT 许可模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动按硬件选型下载模型并提供 OpenAI 兼容本地端点
- replace-api 将付费 API 调用替换为本地端点，改动以 diff 呈现且可 undo
- 零依赖 JS 客户端库与 Rust 一方客户端
- 仅搭载 ungated、Apache-2.0/MIT 许可的模型

## 适用场景

- 开发调试 AI 功能时不产生按次计费
- 本地优先/桌面应用内嵌离线 AI 能力
- 将现有 OpenAI SDK 调用切换为本地免费端点

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L21: Run that in your project and localbrain pulls a lightweight open-source model, stands up a **local, OpenAI-compatib
> L179: Four independent layers — CLI orchestrator, detection engine, adapters, and a model runtime (downloader + `node-ll
> L65: 3. **Serve** an OpenAI-compatible endpoint at `http://localhost:4141/v1`.

## 星数曲线

```mermaid
xychart-beta
    title "kowais915/localbrain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `442b71e359f3` · [字段定义](../../DATASET.md)*
