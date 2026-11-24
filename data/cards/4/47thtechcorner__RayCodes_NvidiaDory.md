# 47thtechcorner/RayCodes_NvidiaDory

⭐ 3 · HTML · 推送 2026-11-06 · [GitHub](https://github.com/47thtechcorner/RayCodes_NvidiaDory) · [官网](https://youtu.be/7QJz4u0cjsE) · 个人维护

**基于 NVIDIA Dory 4B 模型的本地代码审计/抽取生产流水线**

围绕 NVIDIA Nemotron-Labs Dory 1.0（4B looped transformer）构建的生产流水线仓库：模型采用 latent-recurrent 架构，将 20 层内部块每 token 循环最多 4 次，在 4B 静态显存占用下提供 256K 滑窗上下文，内存占用 2.43 GB。仓库提供 Windows PowerShell 环境搭建与运行脚本（python main.py），并给出代码库重构与 bug 审计、网页抽取格式化、多 agent swarm、长合同扫描等测试工作流。模型许可为 OpenMDW-1.1。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4B looped transformer，内存占用 2.43 GB，上下文 256K SWA
- SWE-bench Verified 61.8%（仓库声明数据）
- loop=1 到 loop=4 的动态计算分配，单台 16GB RAM 笔记本并发运行多 agent
- PowerShell 一键环境搭建（venv + pip + python main.py）

## 适用场景

- 本地离线审计 Python 代码库的竞态条件与资源泄漏
- 从原始网页/DOM 转储中抽取结构化 schema
- 在资源受限设备上运行多 agent swarm 分级处理任务
- 扫描 150+ 页合同查找免责条款冲突

## 场景标签

`多智能体` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L6: # NVIDIA Nemotron-Labs Dory 1.0 (4B)
> L16: ## 📊 Production Test Workflows
> L43: - ⚡ **Local Codebase Intelligence**: Ingest full software repositories into native 256K sliding-window context to d

## 星数曲线

```mermaid
xychart-beta
    title "47thtechcorner/RayCodes_NvidiaDory 星数(近 2 点)"
    x-axis ["2026-11-13", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-13 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `5a0bdbc26b1e` · [字段定义](../../DATASET.md)*
