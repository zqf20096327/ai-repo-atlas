# dotberg/pwnagotchi-zero

⭐ 17 · Java · MIT · 推送 2026-10-12 · [GitHub](https://github.com/dotberg/pwnagotchi-zero) · 个人维护

**把 root 安卓手机变为自主 WiFi 安全测试平台**

面向 root 安卓设备的 WiFi 安全测试 APK：通过 Qualcomm qcacld-3.0/adrastea 固件重载技巧启用原生监听模式（无需内核补丁或外接硬件），执行信道跳变扫描、客户端预扫描、CSA+deauth 洪泛（绕过 802.11w PMF）与被动 EAPOL 捕获。内置 Thompson Sampling 贝叶斯多臂老虎机按 AP 学习攻击策略并跨会话持久化。要求 Magisk root、Qualcomm WiFi 与 Termux（tcpdump/iw），首部署需 ADB。已在 Motorola Edge 50 Fusion（Android 14）上测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Qualcomm 固件重载技巧启用原生监听模式，无需内核补丁
- Thompson Sampling 按 AP 学习攻击策略，跨会话持久化
- CSA 信标绕过 PMF（802.11w）的 deauth 洪泛
- 被动 EAPOL 捕获并以 EAPOL 计数后验证

## 适用场景

- 用闲置 root 安卓手机做 WiFi 渗透测试与握手捕获
- 在无外接网卡条件下研究 Qualcomm 监听模式启用方法
- 学习 CSA 绕过 PMF、客户端预扫描等 WiFi 攻击技术

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L29: - **Thompson Sampling AI** — Bayesian bandit per AP. Learns which targets respond. Persists across sessions.
> L175: Pwnagotchi concept and faces (◕‿‿◕) by evilsocket/pwnagotchi. This project is an independent Android-native reimpl

## 星数曲线

```mermaid
xychart-beta
    title "dotberg/pwnagotchi-zero 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `46eb344dc99a` · [字段定义](../../DATASET.md)*
