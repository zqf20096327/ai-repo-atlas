# jeremylongshore/cad-ai-agent

⭐ 46 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/jeremylongshore/cad-ai-agent) · 个人维护

**面向 AEC 专业人员的 DXF/PDF 图纸自然语言编辑与审查平台**

通过自然语言对 DXF/矢量 PDF 图纸（DWG 需另行安装 ODA File Converter）执行操作的平台：LLM 规划器返回结构化 ChangeSet 而不接触原始 DXF 数据，经校验后应用编辑，始终保留原文件。能力包括 13 种编辑操作、ADA/IBC 合规校验、健康报告、工程量统计、图纸摘要、RFI 生成、房间检测、版本比对与地理坐标转换。LLM 提供方可插拔（默认 mock 模式离线可测），提供桌面应用、CLI 与可自托管的 Web 应用（React + FastAPI）。限制：不支持 DWG 原生编辑、3D 实体与外部参照。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 规划器仅输出结构化 ChangeSet，不接触原始 DXF 数据
- 合规校验、工程量统计、RFI 生成、版本比对等能力
- 模型无关的可插拔 LLM 提供方接口
- 默认 mock 提供方支持无 API key 离线测试全流程

## 适用场景

- 用自然语言对 CAD 图纸做移动、复制、文字修改等编辑
- 对图纸做 ADA/IBC 合规检查并获取整改建议
- 自动生成工程量统计、健康报告与图纸摘要
- 比对两个 DXF 版本并审查、应用变更

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: Upload a DXF or vector PDF—or a DWG when the optional ODA File Converter is installed—describe what you need in plai
> L15: **cad-dxf-agent** is a multi-capability platform that handles DXF drawings through natural language. Describe what 
> L34: - **Safe edits** — The LLM planner returns structured operations only. It never touches raw DXF data.

## 星数曲线

```mermaid
xychart-beta
    title "jeremylongshore/cad-ai-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 44 --> 47
    line [45, 46, 46]
```

2026-10-18 45 → 2026-10-26 46（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `d06033973007` · [字段定义](../../DATASET.md)*
