# MaxiDonkey/DelphiAnthropic

⭐ 61 · Pascal · MIT · 推送 2026-09-06 · [GitHub](https://github.com/MaxiDonkey/DelphiAnthropic) · 个人维护

**Delphi 语言的 Anthropic Claude API 非官方封装库**

以 Delphi 12 编写的 Anthropic 公共 API 原生封装（非官方 SDK），面向 Delphi 开发者访问 Claude Messages API 与 Managed Agents。覆盖同步/异步生成、SSE 流式、工具调用、结构化输出、图像与 PDF 多模态输入、扩展/自适应思考、Agent Skills、Webhooks HMAC 验签、批处理与 Prompt 缓存等，并以功能覆盖表标注各能力是否依赖 Anthropic beta 头。附基于 Pythia-WebView2 的 VCL 演示程序。MIT 许可，可免费用 Delphi CE 编译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Messages API 与 Managed Agents（Agent/Environment/Session/Vaults/Memory Stores）双重表面映射
- 同步/异步执行与 SSE 流式，含事件级回调
- 工具调用、结构化输出、多模态输入（图像/PDF）
- Webhook HMAC 常数时间验签与类型化事件分发

## 适用场景

- 在 Delphi 应用中集成 Claude 对话与流式生成
- 构建工具调用与结构化输出的 agent 工作流
- 通过 Managed Agents 驱动服务端长生命周期 agent

## 场景标签

 · 领域:LLM 基础设施/SDK

## 证据(README 行号)

> L46: **DelphiAnthropic** is a native **Delphi wrapper for the Anthropic Claude API**, providing structured access to the
> L70: - **faithful mapping** of both the Messages API and the Managed Agents surface

## 星数曲线

```mermaid
xychart-beta
    title "MaxiDonkey/DelphiAnthropic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-24 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b69c39fa7738` · [字段定义](../../DATASET.md)*
