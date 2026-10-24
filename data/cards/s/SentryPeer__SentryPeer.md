# SentryPeer/SentryPeer

⭐ 212 · C · NOASSERTION · 推送 2026-10-21 · [GitHub](https://github.com/SentryPeer/SentryPeer) · [官网](https://sentrypeer.org) · 个人维护

**SIP 蜜罐欺诈检测工具：收集恶意 IP 与号码并 P2P 共享**

面向 VoIP 服务商与 PBX 运维方的电信欺诈检测工具：以 SIP 蜜罐诱使攻击者发起呼叫，记录其来源 IP 与所拨号码，存入本地 sqlite 数据库，供出站呼叫时通过 RESTful API 查询比对，用于拦截语音邮件欺诈、被盗凭证外呼等场景。支持基于 OpenDHT 的节点间 P2P 数据共享（默认关闭，opt-in），数据归用户所有。可运行于蜜罐模式、纯 API 模式或 DHT 节点模式，C 语言实现，支持 Docker 与多平台安装包。README 中未描述实际的机器学习机制，仅仓库主题标签含 machine-learning。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SIP 蜜罐收集恶意 IP 与被拨号码并存入本地 sqlite
- 基于 OpenDHT 的 P2P 数据共享与复制（默认关闭，opt-in）
- RESTful 查询 API（IP 地址、电话号码）与 WebHook、syslog/Fail2Ban 支持
- 可禁用 SIP 模式，仅作为 API 节点或社区 DHT 节点运行

## 适用场景

- 在自有 VoIP PBX 出站呼叫时查询已知恶意号码并触发告警
- 部署 SIP 蜜罐采集攻击者 IP 用于防火墙/Fail2Ban 联动
- opt-in 加入社区 P2P 网络共享恶意行为数据

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L24: SentryPeer &reg; is a fraud detection tool. It lets bad actors try to make phone calls and saves the IP address the

## 星数曲线

```mermaid
xychart-beta
    title "SentryPeer/SentryPeer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 211 --> 213
    line [212, 212]
```

2026-10-18 212 → 2026-10-24 212（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 low · 依据 README sha `9ebbef8a9c40` · [字段定义](../../DATASET.md)*
