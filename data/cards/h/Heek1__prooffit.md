# Heek1/prooffit

⭐ 3 · C# · MIT · 推送 2026-11-26 · [GitHub](https://github.com/Heek1/prooffit) · [官网](https://prooffit.onrender.com) · 个人维护

**对比简历与职位要求并逐条给出证据支撑匹配报告的工具**

ProofFit 读取 PDF 简历与职位描述，抽取 must-have/nice-to-have 要求，结合候选人公开 GitHub 仓库扫描出的技能事实，对每条要求判定 proven/partly proven/无证据，并计算 0-100 匹配分。每条判定须引用简历行号或 GitHub 文件作为证据，由代码层 EvidenceValidator 校验、算术计分，防止模型编造。提供关键词引擎（默认，无需模型）与 Gemini 模型引擎（可选 API key），模型不可用时回退关键词引擎。技术栈为 ASP.NET Core、React 19、PostgreSQL，支持 OpenTelemetry 观测与防隐藏文字/提示注入处理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每条判定必须指向简历行或 GitHub 文件证据，由代码校验而非信任模型输出
- 双引擎：默认关键词引擎无需模型，配置 Gemini API key 后启用模型引擎并自动回退
- GitHub 技能事实基于规则（文件路径、依赖清单）检测并链接来源文件
- 报告以单一 JSON 文档存储，可导出 PDF 与纯文本摘要，支持 SSE 进度流

## 适用场景

- 投递前核对简历是否真正满足职位硬性要求
- 逐条查看判定所引用的简历原文与 GitHub 证据
- 运行本地评测集比较关键词与模型引擎的准确率

## 场景标签

 · 领域:招聘/求职工具

## 证据(README 行号)

> L16: ProofFit compares a resume with a job posting and backs every verdict with evidence. A
> L55: - The **model engine** asks a language model (Gemini) and is used when an API key is
> L59: Whichever engine runs, its verdicts are only proposals. `EvidenceValidator` drops any cited


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `dbc9c57a61fb` · [字段定义](../../DATASET.md)*
