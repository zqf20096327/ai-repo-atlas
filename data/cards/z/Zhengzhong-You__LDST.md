# Zhengzhong-You/LDST

⭐ 3 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/Zhengzhong-You/LDST) · 组织维护 · 中文 README

**用 LLM 读取求解器日志为科研调参 SCIP 的工具**

研究代码与基准数据集：LLM 在每轮 SCIP 求解后解析日志生成诊断（presolve、根 LP、分支、启发式、界进展），基于 45 参数白名单提出稀疏配置修改，经 schema/域/新颖性校验后实际运行评估；含 SMAC3、RBFOpt、Random 标量反馈基线，四类损失函数按实例求解难度分级，附 215 实例基准（156 个打包生成实例，59 个 MIPLIB 脚本下载并校验 SHA-256）。面向运筹优化研究者复现论文实验，需 SCIP 9.2.4 二进制与 OpenAI API key，仅实现 OpenAI provider。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- LLM 读取求解器日志的诊断式调参，而非仅标量结果反馈
- 45 参数类型化白名单与 schema/域/新颖性校验
- 215 实例基准：CVRP/GAP/JSP/UFL 打包，MIPLIB 下载校验
- 无 LLM 调用的冒烟测试与论文数值复验脚本

## 适用场景

- 复现 MIP 求解器 LLM 调参论文实验
- 对 CVRP、JSP 等实例做单实例配置调优
- 对比语义调参与标量反馈配置器效果

## 场景标签

`提示工程` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L19: Black-box configurators observe one scalar outcome per solver run. LDST instead reads the run itself: after each SC
> L23: The repository contains the LDST implementation, the scalar-feedback baselines (SMAC3, RBFOpt, and Random), and the
> L133: Requests use JSON output and at most 20,000 output tokens; an invalid response is re-queried up to three times. On


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `b0dfce8d3d47` · [字段定义](../../DATASET.md)*
