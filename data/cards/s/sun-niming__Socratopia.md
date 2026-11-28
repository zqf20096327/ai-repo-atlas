# sun-niming/Socratopia

⭐ 3 · HTML · 推送 2026-11-03 · [GitHub](https://github.com/sun-niming/Socratopia) · 个人维护 · 中文 README

**Socratopia 苏格拉底式教学应用的 Windows 工程记录与评测仓库**

记录在无源码、无构建链路条件下对 Socratopia（Electron + Next.js 苏格拉底式教学桌面应用）打包产物做工程实践的分支仓库：对 webpack/esbuild 编译产物做外科式补丁，保留打包运行时可执行文件与全部产品/研究文档。核心内容含 22 个 BUG 的取证台账、LLM 调用账单反解与 Prompt 缓存命中率优化报告、三套带评分锚点的 General Agent 评测任务包，以及 356 个冒烟测试的验证基线。配置文件与 API key 不入库，需自备。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可运行的打包运行时 + 全部产品与研究文档的取证档案
- LLM 调用成本反解与 Prompt 缓存命中率优化文档
- 三套 General Agent 评测任务包（含评分方锚点答案）
- 22 个 BUG 台账与 356 个冒烟测试验证基线

## 适用场景

- 学习如何在无源码条件下对 Electron 打包产物打补丁
- 复用教学类 agent 的评测任务包与锚点答案
- 参考 LLM 成本与缓存优化的取证方法

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: > 公开仓库，记录一次「没有源码、没有构建链路」的系统上做的工程实践：打包产物的外科式补丁、LLM 调用的成本与缓存优化、Windows 文件锁死循环的根因定位，以及一套可直接投喂被测 agent 的评测任务包。运行所需的 `res
> L19: |Agent 评测任务包|`agent-task-datasets/`（三套；含评分方锚点答案）|
> L30: **这是打包产物的仓库，不是可编译的源码树。** 没有构建流水线会从源码重新生成 bundle，所有改动都是对编译产物（webpack/esbuild 输出）的外科式补丁，靠 `node --check` / acorn 加就地冒


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `e508aa7b3a81` · [字段定义](../../DATASET.md)*
