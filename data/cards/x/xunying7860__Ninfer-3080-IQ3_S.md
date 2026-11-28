# xunying7860/Ninfer-3080-IQ3_S

⭐ 3 · C++ · 推送 2026-10-29 · [GitHub](https://github.com/xunying7860/Ninfer-3080-IQ3_S) · 个人维护 · 中文 README

**Qwen3.8-27B IQ3_S 在 RTX 3080 20GB 单卡 Linux 上的部署与运维工具集**

将 NInfer 引擎（bundle 随仓库以 zstd 分卷分发）与 IQ3_S 量化模型配置为 Ubuntu 22.04 上由 systemd 托管的常驻服务，OpenAI 与 Anthropic 双协议接口（端口 18082）。仓库提供启动脚本（含逐次改档理由注释）、活锁指纹看门狗、Web 监控面板（日志 tail / metrics / NVML 数据源）、上下文长度二分脚本与门禁测试套件。附带 KVarN KV 量化移植的补丁系列与 1,026 件对拍取证。模型权重不分发，需自备。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- systemd 常驻部署：单元文件、看门狗、开机锁频降压服务
- 活锁指纹看门狗：GPU 利用率/功耗/计数器三量判定后自动重启
- Web 监控面板读取引擎日志、/metrics、NVML、/proc 的只读数据
- KVarN KV 量化移植 patch 系列（7 份 patch）与逐文件 md5 取证

## 适用场景

- 在单张 sm_86 显卡上把 NInfer + Qwen3.8 部署为常驻推理服务
- 为本地 LLM 服务配置自动故障恢复与运维监控
- 参考 KV 量化方案的实测对拍数据做选型

## 场景标签

`模型量化` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L4: systemd 托管、固定用 GPU0、原生 glibc loader（不需要 Docker、不需要装 Python 环境），
> L9: 本仓库放**把服务跑起来所必需的全部东西**：启动脚本、systemd 单元、看门狗、监控面板，
> L23: |接口|`http://<host>:18082/v1`（OpenAI 与 Anthropic 双协议），`--model-id qwen3.8-27b-gsq-rco-iq3s`|

## 星数曲线

```mermaid
xychart-beta
    title "xunying7860/Ninfer-3080-IQ3_S 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-26 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `eefcedb617d0` · [字段定义](../../DATASET.md)*
