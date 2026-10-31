# vllm-project/vvm

⭐ 14 · Rust · Apache-2.0 · 推送 2026-08-02 · [GitHub](https://github.com/vllm-project/vvm) · 组织维护

**vLLM 版本管理器：用隔离 venv 管理多个 vLLM 安装并即时切换**

面向 vLLM 使用者与开发者的命令行版本管理工具：每个版本（release、nightly、commit、branch、PR、git URL、本地 checkout）安装到独立 venv（~/.vvm/versions/），通过切换 symlink 更新 PATH/VIRTUAL_ENV 实现即时切换。默认从 wheels.vllm.ai 拉取预编译 wheel，缺 wheel 时回退源码编译；--path 模式将预编译 C++/CUDA 匹配到 fork 的 merge-base，--compile 模式在 csrc/cmake 无变化时复用内核。另提供别名、vvm exec、CUDA 变体选择及 flashinfer/DeepGEMM/DeepEP 等配套包安装（按活跃 vllm 的 pin）。单静态二进制，仅需 uv 与 python3，支持 Linux x86_64/aarch64。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按 release/commit/branch/PR/git URL/本地路径安装到隔离 venv 并即时切换
- 默认拉取预编译 wheel，必要时回退源码编译；repeat --compile 复用内核
- CUDA 变体自动检测（nvidia-smi/version.json/nvcc），可选 cu130/cu128/cpu
- install-extra 按活跃 vllm 的 pin 安装 deepgemm/flashinfer/deepep 并验证

## 适用场景

- 在同一台机器上并行测试 vLLM 的多个版本、分支或 PR
- 为 vLLM fork 做可复现的本地开发安装（editable + 预编译 C++/CUDA）
- 为指定 vLLM 版本安装匹配 pin 的 flashinfer/DeepGEMM/DeepEP 配套包
- 在无 nvidia-smi 的登录节点上指定 CUDA 变体安装

## 场景标签

 · 领域:AI 基础设施工具

## 证据(README 行号)

> L3: Manage multiple vLLM installations with isolated Python virtual environments. Switch between releases, commits, bran
> L12: - **Isolated** — every version gets its own venv; no cross-version dependency conflicts.

## 星数曲线

```mermaid
xychart-beta
    title "vllm-project/vvm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `36881e728069` · [字段定义](../../DATASET.md)*
