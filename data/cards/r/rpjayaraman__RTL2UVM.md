# rpjayaraman/RTL2UVM

⭐ 34 · SystemVerilog · MIT · 推送 2026-02-24 · [GitHub](https://github.com/rpjayaraman/RTL2UVM) · 个人维护

**从 Verilog RTL 自动生成 UVM 验证环境的 Python 工具**

面向芯片验证工程师的命令行工具：用 pyslang 解析 Verilog RTL，提取端口信息，生成完整的 SystemVerilog UVM testbench 结构，包括 Interface、Driver、Monitor、Agent、Scoreboard、Coverage、Environment 等十余类文件，并生成 Verilator 仿真 Makefile。可选接入 Gemini（google.generativeai）生成 driver/monitor/scoreboard 逻辑，需 API key。支持 Verilator/EDA Playground 两种仿真模式，可用 pygraphviz 输出 testbench 结构图。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 Verilog RTL 生成完整 UVM testbench 结构（Interface 到 Top 共 12 类文件）
- 可选 LLM（Gemini）辅助生成 driver/monitor/scoreboard 逻辑
- 生成 Verilator 仿真 Makefile，支持覆盖率分析选项
- pygraphviz 可视化 testbench 结构

## 适用场景

- 为新的 Verilog 模块快速搭建 UVM 验证环境骨架
- 配合 Verilator 进行仿真与覆盖率分析
- 用 LLM 辅助编写驱动与记分板逻辑

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L8: `RTL2UVM` is a Python-based tool that automates the creation of SystemVerilog UVM (Universal Verification Methodolog
> L26: * **LLM Integration (Optional):** Leverages Large Language Models (LLMs) like Gemini (via the `google.generativeai`

## 星数曲线

```mermaid
xychart-beta
    title "rpjayaraman/RTL2UVM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-26 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c963ca5900e5` · [字段定义](../../DATASET.md)*
