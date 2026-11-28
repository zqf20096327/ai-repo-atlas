# FlagOpen/SciSage

⭐ 10 · Python · MIT · 推送 2026-08-19 · [GitHub](https://github.com/FlagOpen/SciSage) · [官网](https://arxiv.org/abs/2506.12689) · 组织维护

**面向科研人员的多智能体科学综述自动生成框架**

SciSage 是一个多智能体科学综述生成框架，流程覆盖从 arXiv 抓取论文（含降级回退机制）、AI 驱动的论文理解与大纲生成、到按章节生成带引用的结构化内容。模型配置集中在 model_factory.py，兼容 GPT-4 系列与本地/云端模型；运行需自行配置搜索 API key。仓库另附 SurveyScope 基准数据集与论文抓取工具，MIT 许可，通过 git clone 后 pip 安装依赖运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多智能体流水线：抓取→大纲→分章节生成带引用综述
- 从 arXiv 多源抓取论文并内置降级回退机制
- 支持 GPT-4、本地模型与云服务多种模型接入
- 附带 SurveyScope 基准数据集（发布于 Hugging Face）

## 适用场景

- 为指定研究主题自动生成结构化文献综述
- 构建和评测综述生成任务的基准实验
- 批量抓取 arXiv 论文信息用于研究

## 场景标签

`多智能体` `模型评测` `科研工具` `网页抓取` · 领域:Agent 开发

## 证据(README 行号)

> L11: - **Multi-source Paper Extraction**: Robust crawling from arXiv with fallback mechanisms
> L12: - **Intelligent Analysis**: AI-powered paper understanding and outline generation
> L13: - **Structured Content Generation**: Section-wise detailed analysis with proper citations


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `acba665f4a34` · [字段定义](../../DATASET.md)*
