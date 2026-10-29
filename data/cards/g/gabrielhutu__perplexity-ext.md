# gabrielhutu/perplexity-ext

⭐ 20 · TypeScript · MIT · 推送 2025-12-10 · [GitHub](https://github.com/gabrielhutu/perplexity-ext) · [官网](https://marketplace.visualstudio.com/items?itemName=ghutu.perplexity-ext) · 个人维护

**在 VS Code 内调用 Perplexity API 的聊天扩展**

VS Code 扩展，将 Perplexity AI 的 API 接入编辑器：提供流式聊天回复、引用追踪、模型下拉选择（sonar/sonar-pro/sonar-reasoning/sonar-reasoning-pro/sonar-deep-research，r1-1776 不支持）。API key 通过 VS Code Secret Storage 加密存储，webview 使用 CSP nonce 保护。面向使用 Perplexity 的开发者，可通过 marketplace 安装，或 git clone 后用 vsce 打包成 vsix 手动安装。README 标注 WORK IN PROGRESS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 流式响应与引用追踪
- 6 个可选模型（sonar 系列）
- API key 经 VS Code Secret Storage 加密存储

## 适用场景

- 在 VS Code 内直接向 Perplexity 提问获取带引用的回答
- 编码时切换不同 sonar 模型进行检索问答

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: Integrate Perplexity AI's API directly into VS Code with real-time chat capabilities and streaming responses.
> L9: - **Streaming responses** with incremental output

## 星数曲线

```mermaid
xychart-beta
    title "gabrielhutu/perplexity-ext 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f47646ce37e0` · [字段定义](../../DATASET.md)*
