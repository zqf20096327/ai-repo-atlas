# geer1895/rfauto

⭐ 22 · Python · GPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/geer1895/rfauto) · 个人维护 · 中文 README

**RF/微波设计自动化框架，AI agent 经 MCP 驱动全部流程**

面向 RF/微波工程师的自动化设计循环：以 YAML 配方描述器件，从闭式物理推导初猜尺寸，经统一适配层调用 16 个 EM/EDA 求解引擎（HFSS、ADS、openEMS、COMSOL 等），结果过六类质量门（端口语义、网格伪影、物理不变量等），再做 TPE/CMA-ES/NSGA-II 优化。内置 fake 通道可无许可跑通全流程。157 个 MCP 工具让 Claude Desktop/Cursor 等 agent 驱动全部功能，但规定每个物理数字必须来自确定性内核或求解器，不由语言模型生成。附本地 Web 工作台（24 视图）与 87 个校准锚点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 16 个求解引擎统一适配层，内置 fake 通道无需商业许可即可运行全流程
- 157 个 MCP 工具供 AI agent 驱动，物理数字仅由确定性内核或求解器产出
- 75 个参数化器件模板 + 340 个确定性计算器 + 87 个校准锚点
- 六类质量门拦截求解器静默失败（端口语义/网格伪影/物理不变量等）

## 适用场景

- 用一份 YAML 配方完成微波器件的合成、仿真、质检与优化闭环
- 让 Claude Desktop/Cursor 中的 agent 经 MCP 自动驱动整个设计流程
- 多引擎交叉仲裁与校准锚点核验仿真结果可信度

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L12: **rfauto turns RF/microwave design from "draw, wait for the solver, copy
> L155: **157 MCP tools** and 10 resources: Claude Desktop, Cursor or your own agent can
> L157: validation gates before touching the workspace; the agent emits typed tool calls


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `4183b01a2076` · [字段定义](../../DATASET.md)*
