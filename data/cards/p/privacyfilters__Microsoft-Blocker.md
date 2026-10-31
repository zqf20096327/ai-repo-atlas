# privacyfilters/Microsoft-Blocker

⭐ 14 · GPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/privacyfilters/Microsoft-Blocker) · 个人维护

**屏蔽 Microsoft 遥测与服务的域名过滤清单（三档强度）**

一组用于 DNS/广告拦截工具的过滤清单，目标是拦截 Microsoft 服务、遥测、跟踪与分析连接。提供 Lite、Proper、No Microsoft 三档强度：Lite 保留 Outlook/Office/OneDrive/Teams 等服务；Proper 保留 Windows 更新、Defender、Winget 等必要功能；No Microsoft 档会连带阻断 Windows 更新与 Defender 定义更新。清单提供 Adblock/DNS、Domains、DNSMasq、Hosts 四种格式，可被 AdGuard Home、Pi-hole、uBlock Origin、AdAway 等工具订阅，另附需手动放行的 whitelist。作者声明部分服务会被破坏，Codeberg 为主仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三档强度：Lite/Proper/No Microsoft，覆盖不同保留需求
- 四种格式：Adblock/DNS、Domains、DNSMasq、Hosts
- 兼容 AdGuard Home、Pi-hole、uBlock Origin、AdAway、pfBlockerNG 等工具
- 提供配套 whitelist 供需手动放行的工具使用

## 适用场景

- 在网络级 DNS 拦截器上阻断 Microsoft 遥测与跟踪域名
- 按需选择保留 Windows 更新/Office 或完全阻断的过滤强度
- 为 Pi-hole、AdAway 等工具订阅域名屏蔽清单

## 场景标签

 · 领域:网络隐私/域名过滤

## 证据(README 行号)

> L5: Microsoft Blocker is a collection of filters for blocking Microsoft services, telemetry, tracking, analytics, and ot
> L19: These filters work best with **network-wide DNS blockers** (AdGuard Home, Pi-hole, router adblockers). See Recommen

## 星数曲线

```mermaid
xychart-beta
    title "privacyfilters/Microsoft-Blocker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `4b73190ff194` · [字段定义](../../DATASET.md)*
