# weiber2002/ICRTL-Benchmark

⭐ 35 · SystemVerilog · 推送 2026-07-03 · [GitHub](https://github.com/weiber2002/ICRTL-Benchmark) · 组织维护 · 中文 README

**给EDA/LLM研究者的工业级Verilog RTL基准测试集（10题）**

来自台湾积体电路设计竞赛与手工命题的工业级 Verilog RTL 设计挑战集合，含10个题目（LBP、卷积、霍夫曼编码、脉动阵列GEMM等），每题提供规格说明、testbench、golden数据与参考实现，用于评估LLM在RTL设计与PPA优化上的能力。全流程兼容开源工具链（Icarus Verilog+Yosys+NanGate45 PDK），参考实现不依赖DesignWare等专有IP；另提供基于Synopsys VCS/DC/PT的商业工具评估流程。规格含中文原版PDF，另提供LLM可读的SPEC.md。

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

- 10个工业级RTL题目，覆盖加速器、压缩、搜索、图像处理等模块
- 每题含SPEC、testbench、golden数据与可在Yosys运行的参考实现
- 100%开源兼容流程（iverilog+Yosys+NanGate45），不依赖专有IP
- 附带LLM可读SPEC.md与Python评估框架（VCS/DC/PT流程）

## 适用场景

- 评估LLM生成RTL代码与PPA优化的能力
- 在开源EDA工具链上跑RTL综合与仿真基准
- 为RTL设计自动化研究提供带参考实现的测试集

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: This repository presents the **ICRTL Benchmark**, a comprehensive collection of industrial-level **Verilog RTL desig
> L5: Each challenge targets specific algorithms and hardware modules utilized in the modern IC industry. We designed this
> L37: * `SPEC.md`: LLM-readable SPEC extracted from Original_SPEC, including a description of the current implementation.

## 星数曲线

```mermaid
xychart-beta
    title "weiber2002/ICRTL-Benchmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-31 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `eed44bdfc1d2` · [字段定义](../../DATASET.md)*
