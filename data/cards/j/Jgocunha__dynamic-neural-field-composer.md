# Jgocunha/dynamic-neural-field-composer

⭐ 19 · C++ · MIT · 推送 2026-10-09 · [GitHub](https://github.com/Jgocunha/dynamic-neural-field-composer) · [官网](https://youtu.be/Ss_FOccIM_o) · 个人维护

**构建与仿真动态神经场（DNF）架构的 C++20 库与交互应用**

面向认知神经科学与认知机器人研究者的 C++20 库及交互式应用：以编程方式或 ImGui 可视化节点图编辑器设计、连接、仿真动态神经场架构，实时绘制场激活、输出与输入，架构可序列化为 JSON 并重新加载。提供 NeuralField、多种核函数、刺激、噪声、耦合、记忆痕迹等 1D/2D 元素，库可嵌入任意 C++ 应用。Releases 页提供预编译二进制，也可用脚本从源码构建；源码构建需手动安装编译工具链（VS2022/GCC 13+/Xcode CLT、CMake），其余依赖由 setup 脚本自动安装。产出两个启动器：固定布局版与可停靠窗口版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 编程 API 与 ImGui 可视化节点图编辑器两种方式搭建 DNF 架构
- NeuralField、Gauss/MexicanHat 等核、刺激、噪声、耦合、记忆痕迹等 1D/2D 元素库
- 架构可保存/重载为 JSON，仿真实时绘图监控
- 库可链接嵌入任意 C++ 应用，Releases 提供免构建的预编译二进制

## 适用场景

- 用可视化节点图实时搭建并观察神经场仿真（工作记忆、赢家通吃、序列生成）
- 在 C++ 项目中嵌入 DNF 仿真做认知机器人研究
- 复现并扩展论文中的 DNF 架构实验

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L21: Dynamic Neural Fields model how neuron populations represent and transform information over continuous dimensions (
> L23: This library lets you design, connect, simulate, and visualize DNF architectures at runtime, either programmaticall
> L25: - **Compose architectures in C++** — wire up fields, kernels, stimuli, and couplings in a few lines

## 星数曲线

```mermaid
xychart-beta
    title "Jgocunha/dynamic-neural-field-composer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-31 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `10942561d12d` · [字段定义](../../DATASET.md)*
