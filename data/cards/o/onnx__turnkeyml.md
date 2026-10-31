# onnx/turnkeyml

⭐ 247 · Python · Apache-2.0 · 推送 2026-07-01 · [GitHub](https://github.com/onnx/turnkeyml) · 组织维护

**ONNX 工作流的无代码 CLI 工具链（导出/优化模型）**

ONNX 生态工具集项目：turnkey 提供面向通用 ONNX 工作流（如 CNN 与 Transformer 的导出、优化）的无代码 CLI，通过 `turnkey -h` 列出支持的命令。项目曾包含面向 LLM 的 Lemonade SDK，该部分已迁移至独立仓库 lemonade-sdk/lemonade（新 PyPI 包名 lemonade-sdk），README 要求用户尽快迁移。turnkey 仍在维护，由 ONNX Model Zoo SIG 赞助、AMD 人员维护，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无代码 CLI 覆盖通用 ONNX 工作流（导出/优化 CNN 与 Transformer）
- 曾提供 LLM 全栈 SDK Lemonade，已迁移为独立项目 lemonade-sdk
- 由 ONNX Model Zoo SIG 赞助，Apache 2.0 许可

## 适用场景

- 不写代码即可执行 ONNX 模型的导出与优化流程
- 作为 ONNX 生态工具的统一命令行入口
- LLM 场景需迁移至 lemonade-sdk 新包继续使用

## 场景标签

 · 领域:模型工具链/ONNX 生态

## 证据(README 行号)

> L8: We are on a mission to make it easy to use the most important tools in the ONNX ecosystem. TurnkeyML accomplishes th
> L29: While Lemonade focuses on LLMs, Turnkey is a no-code CLI designed for general ONNX workflows, such as exporting and

## 星数曲线

```mermaid
xychart-beta
    title "onnx/turnkeyml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 246 --> 248
    line [247, 247]
```

2026-10-18 247 → 2026-10-31 247（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 low · 依据 README sha `f517465d9547` · [字段定义](../../DATASET.md)*
