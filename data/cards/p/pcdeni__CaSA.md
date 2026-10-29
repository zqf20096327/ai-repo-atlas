# pcdeni/CaSA

⭐ 22 · C++ · MIT · 推送 2026-08-17 · [GitHub](https://github.com/pcdeni/CaSA) · 组织维护

**在 DDR4 内存芯片内以电荷共享 PIM 运行 LLM 的软件栈**

SAFARI 系研究背景的演示项目软件部分：在未改装的 DDR4 DIMM 上，利用多行电荷共享的多数投票机制执行 LLM 的投影矩阵乘法，权重常驻内存单元；attention、softmax、采样等仍由宿主机 PyTorch 执行。支持 BitNet b1.58-2B-4T 等 7 个模型家族，实测 45 s/token。仓库含 C++ 应用、transformers 补丁编排器、MVDRAM 复现服务、RTL 读回引擎与 DDR4 调度器，需配合 DRAM-Bender FPGA 平台与专用硬件运行。

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

- 投影矩阵乘法在 DDR4 DIMM 内以电荷共享多数投票执行
- 支持 BitNet b1.58-2B-4T、Llama2/3、Phi-4 等 7 个模型家族
- 实测从 632 s/token 降至 45 s/token，目标为 DDR-PHY-bound 下限
- 含 MVDRAM（arXiv 2503.23817）复现与 Verilator RTL 验证

## 适用场景

- 在真实 DRAM-Bender 硅片上复现片内 LLM 推理演示
- 研究存内计算运行 ternary/1-bit 量化模型的延迟边界
- 基于补丁将 transformers 投影层路由到 FPGA 侧服务器做实验

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L14: The host runs attention softmax, norms, and sampling in PyTorch, exactly as
> L50: - **`app/`** — C++ apps that issue charge-sharing primitives on real
> L53: - **`python/`** — orchestrator that patches Hugging Face `transformers` to

## 星数曲线

```mermaid
xychart-beta
    title "pcdeni/CaSA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `9d4a8c79616d` · [字段定义](../../DATASET.md)*
