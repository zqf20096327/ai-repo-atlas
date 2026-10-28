# docxology/template

⭐ 20 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/docxology/template) · [官网](https://doi.org/10.5281/zenodo.19139090) · 个人维护

**可复现计算研究的项目模板：17 阶段流水线与出版链**

面向 Python 3.12+ 的研究项目脚手架（GitHub Template），通过两层架构（共享 infrastructure 层 + 互相独立的 projects 工作区）约束代码、测试、手稿与出处的完整性：提供 17 阶段 DAG 流水线（环境→测试→PDF→哈希产物）、零 Mock 测试策略与覆盖率门槛、SHA-256/512 哈希与 PDF 隐写水印的加密出处机制。面向编码 agent 提供目录级 AGENTS.md/SKILL.md 路由与技能清单。通过 GitHub template 创建仓库后用 uv sync 安装、run.sh 运行；附带 Docker 云端部署目录与 CI 检查。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 17 阶段 DAG 流水线：环境设置→测试→PDF→哈希产物
- 零 Mock 策略与覆盖率门槛（项目 src ≥90%、基础设施 ≥60%）
- SHA-256/512 哈希 + PDF 隐写水印的加密出处机制
- 目录级 AGENTS.md/SKILL.md 与技能清单的 agent 路由体系

## 适用场景

- 以模板创建新的可复现研究仓库
- 让编码 agent 按路由文件定位任务并遵循流水线约束
- 多项目共享一层基础设施、各自产出带出处的 PDF 手稿

## 场景标签

 · 领域:科研工程化/项目模板

## 证据(README 行号)

> L15: Pipelines · Manuscripts · Cryptographic Provenance · AI-Agent Collaboration
> L135: |**AI-agent-ready codebase**|`AGENTS.md` + `README.md` per directory; `SKILL.md` + `.agents/skill_manifest.json` f

## 星数曲线

```mermaid
xychart-beta
    title "docxology/template 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 low · 依据 README sha `9178f0d48fcc` · [字段定义](../../DATASET.md)*
