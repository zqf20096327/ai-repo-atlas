# idlab-discover/RustiFlow

⭐ 28 · Rust · MIT · 推送 2026-10-21 · [GitHub](https://github.com/idlab-discover/RustiFlow) · [官网](https://idlab-discover.github.io/RustiFlow) · 组织维护

**Rust+eBPF 的网络流量特征提取工具，面向入侵检测等场景**

基于 Rust 与 eBPF（Aya 库）的网络流特征提取命令行工具，面向网络入侵检测系统与网络安全应用的开发者/研究者。支持实时捕获（仅 Linux，依赖 eBPF 与 tc）与离线 pcap 读取，覆盖 IPv4/IPv6 上 TCP/UDP/ICMP 等协议；提供多种预定义特征集（如 CIDDS、CIC）并支持自定义。输出可到控制台或 CSV，带 TUI 配置界面、Docker 镜像与预编译二进制；不重组分片报文，不做完整 TCP 流重组。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- eBPF 实时捕获（仅 Linux）与离线 pcap 双模式
- 预定义特征集（CIDDS/NFlow 等）与自定义特征集
- TUI 界面、配置文件、CSV 导出与 early-export 周期快照
- Docker 容器与 release 预编译二进制两种分发方式

## 适用场景

- 为网络入侵检测系统提取流特征
- 从已捕获的 pcap 文件生成数据集
- 对网卡流量做实时特征提取与监控

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7: This tool is engineered for robust and efficient feature extraction, particularly for applications such as network i
> L19: - **Versatile Feature Sets:** Offers a variety of pre-defined feature sets (flows) and the flexibility to create cu

## 星数曲线

```mermaid
xychart-beta
    title "idlab-discover/RustiFlow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-31 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `7a6cf21910cd` · [字段定义](../../DATASET.md)*
