# hiruhiru2005/sync-strata

⭐ 115 · JavaScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/hiruhiru2005/sync-strata) · 个人维护

**在单台家用 PC 上一键运行 125B MoE 模型的本地 LLM 应用**

基于 Strata 引擎 fork 的本地推理发行版，随附 Sync-XS/S/M 三档再量化模型与聊天应用 dsh；安装程序按 GPU 自动下载匹配引擎，按内存自动选模型。桌面、手机（同 Wi-Fi 扫码）、命令行与 OpenAI/Anthropic 兼容 API 均可访问。仅支持 Windows 10/11 与 glibc 2.28+ Linux，需 AVX2 CPU 与 ≥8GB 显存 GPU；模型与引擎格式不兼容上游 Strata 与 llama.cpp。实验性项目，Mac 不支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 按 GPU 自动下载匹配引擎，按 RAM 自动选择 XS/S/M 模型
- 提供 OpenAI 兼容 /v1 与 Anthropic 兼容 /v1/messages API
- 手机扫码接入（一次性 3 分钟有效的通行码）
- tail skip（R4/R7/R10）与 KV 量化（k8v4/k4）可调

## 适用场景

- 在带 RTX 30/40 显卡家用电脑上本地运行大模型对话
- 同一 Wi-Fi 下用手机访问家里 PC 上的模型
- 通过本地 OpenAI 兼容 API 接入自己的应用

## 场景标签

`推理引擎` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L6: The engine is a fork of Strata, and the models, **Sync-XS, Sync-S and Sync-M**, are re-quantized to run faster than 
> L73: - **API**: `http://127.0.0.1:8080/v1` (8080 is the default port; if another program is using it, the app moves to a

## 星数曲线

```mermaid
xychart-beta
    title "hiruhiru2005/sync-strata 星数(近 8 点)"
    x-axis ["2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 7 --> 124
    line [16, 61, 75, 85, 88, 99, 110, 115]
```

2026-11-19 16 → 2026-11-27 115（+99）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `992000be6191` · [字段定义](../../DATASET.md)*
