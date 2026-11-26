# abhiramasonny/jaithon

⭐ 45 · Jai · MIT · 推送 2026-10-08 · [GitHub](https://github.com/abhiramasonny/jaithon) · 个人维护

**Java/Python 风格的垃圾回收语言，字节码 VM + JIT，附 Metal GPU 科学计算库**

用 C 实现的动态执行、垃圾回收语言，架构借鉴 Java，语法受 Python/Rust 影响，含字节码 VM 与 JIT。标准库外附多个 GPU 包：OpenCV 风格计算机视觉（jaicv）、pandas 风格数据帧（jaiframe）、numpy 风格张量（jainum）、scipy 风格科学计算（jaisci），以及 Metal 常驻张量、autograd 与 Keras 风格 Sequential 训练库（jaitensor）。从源码构建需 C11 编译器与 make；macOS 上 Metal/Cocoa 框架启用 GUI 与 GPU 模块。README 声明约 80% 代码由 Claude Code 等 agentic 工具辅助生成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 字节码 VM + JIT 解释器，C11 实现，make 构建
- Metal GPU 移植的 numpy/pandas/OpenCV/scipy 风格库
- jaitensor：Metal 张量、autograd、Keras 风格 Sequential 训练库
- 七百余条 jaicv 用例与真实 OpenCV 录制结果回放校验

## 适用场景

- 在 Apple Silicon GPU 上运行 OpenCV/pandas/numpy 风格的科学计算
- 用 Keras 风格 API 在 Metal 上训练 MNIST 等分类模型
- 学习字节码 VM、JIT 与垃圾回收的语言实现

## 场景标签

 · 领域:编程语言/科学计算

## 证据(README 行号)

> L11: Jaithon is a dynamically executed and garbage collected language with a
> L110: `jaitensor` is GPU-first training: Metal-resident tensors, autograd, and a
> L146: source --> lexer --> parser --> resolver --> type checker --> codegen --> VM


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `81fe99519503` · [字段定义](../../DATASET.md)*
