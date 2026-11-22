# jpsanders/pascal-llm-stack

⭐ 3 · Shell · MIT · 推送 2026-11-17 · [GitHub](https://github.com/jpsanders/pascal-llm-stack) · [官网](https://jamesphillipsanders.com) · 个人维护

**让 2016 年 Pascal GPU 在最新 Ubuntu 上跑本地 LLM 的脚本栈**

针对 GTX 1060（Pascal sm_61）在 Ubuntu 26.04 / kernel 7.0 上运行本地 LLM 的可执行配方：补丁 NVIDIA 570 驱动以支持 kernel 7.0，绕过 apt 包陷阱用 runfile 安装 CUDA 12.8，修 libxml2/glibc 兼容问题，以三个 cmake 参数构建 llama.cpp，并用 Tailscale 将 llama-server 暴露到私有网络。提供 `pascal-llm` 命令按序执行十个步骤，附内核更新后的冒烟测试（PASS/WARN/FAIL 判定与基准对比），README 记录每一步踩坑原因与 llama-bench 实测数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- NVIDIA 570 驱动的 kernel 7.0 补丁（4 处内核 API 重写的版本守卫修复）
- CUDA 12.8 安装的 libxml2 SONAME 与 glibc C23 数学声明修复
- llama.cpp Pascal 构建脚本（GGML_CUDA=ON、CUDA_ARCHITECTURES=61）
- 内核更新后的自动冒烟测试，带 t/s 基线与退出码区分 GPU/工作负载故障

## 适用场景

- 在仅支持到驱动分支 570 的旧 GPU 上跑最新 Ubuntu 与本地 LLM
- 内核升级后自动验证 NVIDIA 驱动与推理服务仍正常
- 通过 Tailscale 在个人设备间安全访问本地 llama-server API

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L13: A working recipe for running local LLMs on a Pascal-era GPU (GTX 1060) under the newest Ubuntu and the newest kerne
> L24: sudo ./pascal-llm run driver           # then build-tools, cuda, llama, services, tailscale, smoke-test
> L87: `03-inference/build-llama-cpp.sh` contains them: `-DCMAKE_CUDA_COMPILER` pointed at nvcc explicitly (cmake does not


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `e7a982eac8e0` · [字段定义](../../DATASET.md)*
