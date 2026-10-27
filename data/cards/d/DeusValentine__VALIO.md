# DeusValentine/VALIO

⭐ 22 · ABAP · Apache-2.0 · 推送 2026-07-30 · [GitHub](https://github.com/DeusValentine/VALIO) · 组织维护

**ABAP 开发者用的 SAP 系统内 AI 代码评审工具**

运行在 SAP 系统中的 ABAP 程序，对 ABAP 类、函数模块与报表执行自动化 AI 代码评审。用户接入任一 SAP 官方允许使用的推理 LLM API（SAP Joule、OpenAI、Anthropic、Azure OpenAI 或本地模型），自行实现一个调用 LLM 的方法后即可使用。支持按传输请求号或对象名选择评审对象，提供 Quick（整体评审）与 Detailed（逐方法评审）两种模式、可自定义并保存提示词，输出 ALV 表格、纯文本或 Excel 三种格式。安装方式为将程序代码复制到本地对象，不依赖 abapGit。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 ABAP 类、函数模块与报表三类对象的自动评审
- 可接入任意 SAP 官方允许的推理 LLM API（含本地模型）
- Quick / Detailed 两种评审模式，Detailed 按方法逐个处理
- 自定义提示词可保存为变体，支持 ALV/文本/Excel 输出

## 适用场景

- 在传输请求发布前自动检查 ABAP 代码问题
- 提交评审前先自查代码、减少返工轮次
- 针对性能、SOLID 原则等特定维度定制评审场景

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L9: An open-source SAP ABAP Tool that performs automatic code reviews using AI.
> L26: You need access to any reasoning LLM API SAP officially allows to use (SAP Joule, OpenAI, Anthropic, Azure OpenAI, 

## 星数曲线

```mermaid
xychart-beta
    title "DeusValentine/VALIO 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a8d444f9a2cd` · [字段定义](../../DATASET.md)*
