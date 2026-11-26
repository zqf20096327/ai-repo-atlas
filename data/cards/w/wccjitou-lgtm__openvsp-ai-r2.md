# wccjitou-lgtm/openvsp-ai-r2

⭐ 3 · Python · NOASSERTION · 推送 2026-11-02 · [GitHub](https://github.com/wccjitou-lgtm/openvsp-ai-r2) · 个人维护 · 中文 README

**基于 OpenVSP 的简体中文 AI 辅助飞行器概念设计原型**

在 OpenVSP 3.51.3 源码上叠加的 AI 辅助层：从自然语言或文档输入出发，经机翼/尾翼/机身 sizing、OpenVSP 建模、VSPAERO 分析、稳定性检查后生成 Word 报告，支持常规、飞翼、鸭翼、串列翼四类布局。提供中文 GUI AI 面板与 MCP stdio 服务器，兼容 OpenAI 格式 API，无 Key 时可离线规则设计。定位为研究原型，报告标注 evidence_status=incomplete，不包含 OpenVSP 二进制与商业翼型数据库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自然语言/文档输入到 sizing、建模、VSPAERO 分析、Word 报告的完整流程
- 支持常规、飞翼、鸭翼、串列翼四类布局
- MCP stdio 服务器提供建模、几何查询、VSPAERO、报告工具
- 无 API Key 时可离线规则设计

## 适用场景

- 用中文自然语言描述需求生成飞行器概念方案
- 对已有设计做参数级迭代修改并重新出报告
- 通过 MCP 让外部 Agent 调用 OpenVSP 建模与分析

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: **OpenVSP 3.51.3 简体中文 AI 辅助飞行器概念设计 / OpenVSP AI-assisted concept design overlay**
> L9: - 简体中文 AI 设计面板（OpenAI 兼容 API；无 Key 可离线规则设计）；
> L10: - 自然语言/文档输入 → 机翼/尾翼/机身 sizing → OpenVSP 建模 → VSPAERO → 稳定性检查 → Word 报告；


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `a54bb86d3600` · [字段定义](../../DATASET.md)*
