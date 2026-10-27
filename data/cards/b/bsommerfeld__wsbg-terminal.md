# bsommerfeld/wsbg-terminal

⭐ 22 · Java · AGPL-3.0 · 推送 2026-09-30 · [GitHub](https://github.com/bsommerfeld/wsbg-terminal) · [官网](https://wsbg.app) · 个人维护

**面向 r/wallstreetbetsGER 的本地 AI 财经行情终端**

为德语 subreddit r/wallstreetbetsGER 用户构建的桌面行情终端：自动抓取最新帖子，用本地运行（Ollama）的 AI 模型生成标题摘要，叠加实时行情（Lang & Schwarz 日间、US 盘后至凌晨 2 点）、280+ 来源的新闻三角去重、CNN 恐惧与贪婪指数、EUR/USD 与金融 Juice 新闻滚动条及国际市场时间。AI 部分完全本地运行，无需云服务或订阅。提供安装器（自动下载 Ollama 与模型），要求 16GB 以上内存与约 15GB 磁盘，支持 macOS（Apple Silicon 优先）、Windows 与 Linux。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动抓取 subreddit 帖子并用本地 AI 生成摘要标题（Ollama，无云依赖）
- 280+ 新闻源三角化与去重，实时行情直接挂在标题旁
- CNN 恐惧与贪婪指数、EUR/USD 与新闻滚动条、国际市场时间
- 安装器自动下载 Ollama 并安装本地模型

## 适用场景

- 在桌面终端集中查看 subreddit 帖子、行情与新闻，无需手动刷新
- 用本地 AI 摘要快速了解帖子讨论的多空倾向
- 在本地运行 AI 保持数据不外传

## 场景标签

 · 领域:金融信息/桌面终端

## 证据(README 行号)

> L19: |**KI-Headlines**|Das Terminal fasst das Affengeschrei zusammen, damit ihr wisst, ob Long oder Short.|
> L26: |**100 % Lokal**|Die KI läuft komplett auf eurer Kiste. Keine Cloud, kein Abo, kein fremder Mensch - eure Verluste 
> L38: Deshalb ist unser *Software-Setup* komplett idiotensicher. Der Installer nimmt euch an die Hand, lädt im Hintergrun

## 星数曲线

```mermaid
xychart-beta
    title "bsommerfeld/wsbg-terminal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `8b61b0aa5a81` · [字段定义](../../DATASET.md)*
