# alessandrolattao/FastFlowLM

⭐ 17 · Makefile · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/alessandrolattao/FastFlowLM) · [官网](https://copr.fedorainfracloud.org/coprs/alessandrolattao/fastflowlm) · 个人维护

**为 Fedora/RHEL 系发行版打包 FastFlowLM，在 AMD NPU 上跑 LLM**

社区维护的 COPR RPM 打包仓库，将 FastFlowLM（AMD Ryzen AI XDNA2 NPU 上运行 LLM 的 CLI 与运行时，MIT）与 xdna-driver（用户态驱动、XRT 库、NPU 固件、DKMS 内核模块，Apache-2.0）打包为 Fedora/AlmaLinux/Rocky/RHEL 可安装的 RPM。安装后需重启激活 NPU 驱动，并用 flm-fetch-kernels 从官方 GitHub 下载不可再分发的专有 NPU 内核二进制（受专有许可约束）。仅支持 XDNA2 NPU 的 Ryzen AI CPU，内核要求 >=6.10。非官方仓库，与 FastFlowLM Inc. 或 AMD 无隶属关系。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 dnf/COPR 一键安装 FastFlowLM 运行时与 XDNA NPU 驱动
- DKMS 自动构建内核模块；内核 7+ 默认用 in-tree amdxdna 驱动，可切换 0.15 版 DKMS 模块
- flm-fetch-kernels 从官方 GitHub 下载专有 NPU 内核二进制到 /opt/fastflowlm
- 提供 flm validate 检测 NPU、flm run 运行模型（如 llama3.2:1b）

## 适用场景

- 在 Fedora/RHEL 系 Linux 上用 AMD Ryzen AI NPU 本地运行 LLM
- 为 Strix/Strix Halo 等 XDNA2 平台安装和维护 NPU 驱动
- 通过 flm CLI 验证 NPU 可用性并运行模型

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L8: FastFlowLM runs large language models on AMD Ryzen AI XDNA2 NPUs.
> L131: |`fastflowlm`|FastFlowLM CLI and runtime (MIT license)|


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `412e6fad33e5` · [字段定义](../../DATASET.md)*
