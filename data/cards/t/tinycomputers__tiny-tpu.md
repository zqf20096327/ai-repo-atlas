# tinycomputers/tiny-tpu

⭐ 18 · Astro · MIT · 推送 2026-10-27 · [GitHub](https://github.com/tinycomputers/tiny-tpu) · [官网](https://tiny-tpu.vercel.app) · 个人维护

**可在浏览器观看运行的 4×4 脉动阵列 TPU RTL 可视化**

用 SystemVerilog 实现的可综合 4×4 权重驻留脉动阵列，计算 int8 矩阵乘法（14 时钟周期）。通过 Verilator 编译为周期精确 C++，再经 Emscripten 编译为 WebAssembly，在浏览器中逐周期执行真实 RTL 并可视化每个 PE、激活与部分和，前端不做任何数学重实现。RTL 输出经 cocotb+numpy 位精确验证，可不经修改用于 FPGA 综合工具。RTL 构建需 WSL2 Ubuntu 环境，提供线上可视化页面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可综合 SystemVerilog 4×4 脉动阵列，int8 输入 / int32 累加，14 周期完成矩阵乘
- Verilator→Emscripten→WebAssembly 流水线，浏览器逐周期运行真实 RTL
- cocotb + numpy 位精确黄金验证（20+ 随机矩阵对）
- 大于 4×4 的矩阵以 4×4 分块多趟执行

## 适用场景

- 在浏览器中逐周期观察脉动阵列硬件结构与数据流
- 学习 TPU 权重驻留数据流与对角偏移调度
- 将该可综合 RTL 用于 FPGA 综合或教学

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L7:  A real, synthesizable 4×4 systolic array in SystemVerilog,
> L52: A 4×4 weight-stationary systolic array computes `C = A · B` for signed int8 matrices in **14 clock cycles**:
> L64: psum_out  <=  psum_in  +  (weight_reg  ×  act_in)

## 星数曲线

```mermaid
xychart-beta
    title "tinycomputers/tiny-tpu 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-26 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 low · 依据 README sha `b727d7969955` · [字段定义](../../DATASET.md)*
