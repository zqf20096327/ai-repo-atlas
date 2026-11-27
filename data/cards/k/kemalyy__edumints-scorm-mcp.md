# kemalyy/edumints-scorm-mcp

⭐ 10 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/kemalyy/edumints-scorm-mcp) · [官网](https://mcp.edumints.com) · 组织维护

**面向 AI 用户的 SCORM 在线课程编译 MCP 服务器**

将课程生产视作基础设施的 MCP 服务器：AI 客户端（作者）以结构化 spec 描述课程，服务器完成校验、主题渲染、无障碍 HTML 输出、SCORM runtime 桥接与打包，产出可在任意 LMS 运行的自包含 zip。服务器端确定性运行、无 LLM 参与。提供 46 个 MCP 工具、31 种屏幕类型、组合式游戏引擎与自适应练习（Elo/BKT）、SCORM 1.2/2004 追踪、xAPI 遥测与 QTI 2.1 导出；CI 内置 XSD 校验、SCORM Cloud 导入与行为探针三重证据链。支持托管端点、Docker 与本地 Python 三种部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 46 个 MCP 工具，单次 build_from_spec 即可生成 SCORM zip
- 31 种屏幕类型与组合式游戏引擎，自适应练习用 Elo/BKT 估计熟练度
- CI 证据链：官方 XSD 校验 + SCORM Cloud 实际导入 + Chromium 行为探针
- 三种部署方式：托管 MCP 端点、Docker 自托管、本地 Python

## 适用场景

- 让 Claude 等 MCP 客户端把一段课程需求直接编译为可上传 LMS 的 SCORM 包
- 企业培训/网络安全意识课程等内容团队批量产出标准化课件
- 需要确定性、可自托管、无供应商锁定的课程编译流水线

## 场景标签

 · 领域:教育科技/e-learning 课件生产

## 证据(README 行号)

> L9: > You (or an AI client like Claude) are the **author**; this server is the **compiler**.
> L12: > Deterministic — **no LLM runs on the server**.
> L33: production as **infrastructure for AI agents** instead:


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 low · 依据 README sha `459526284440` · [字段定义](../../DATASET.md)*
