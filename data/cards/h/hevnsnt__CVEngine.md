# hevnsnt/CVEngine

⭐ 817 · Python · GPL-3.0 · 推送 2026-11-27 · [GitHub](https://github.com/hevnsnt/CVEngine) · 个人维护

**自托管外部攻击面评估平台，AI 辅助 CVE 验证与误报筛除**

cvENGINE 是自托管的外部攻击面与漏洞评估平台：输入域名后持续发现暴露的子域名、地址与证书，构建可搜索的 Shodan 风格清单，并用 bbot、Nmap、Nuclei 等固定版本的开源扫描器评估每台主机。核心机制是 CVE 流（CISA KEV、EPSS 等，每 30-60 分钟读取）按产品与受影响版本范围匹配主机，再由 Sentinel 用六种只读检查复现发现并保留证据。AI 功能默认关闭：可起草只读检测模板（经双重验证）、复核发现分级，主机名脱敏、无工具权限、模型不能单独确认发现，带每日上限与预算控制；无模型时平台仍可运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全天读取 CVE 源并按版本范围匹配受影响主机，一小时内标记已利用 CVE
- Sentinel 用六种只读检查复现发现并保留命令与结果证据
- AI 起草的检测模板需经语法、回环对照、离线测试与二次 AI 审查后才运行
- 支持 Anthropic/OpenAI/OpenRouter 或本地 Ollama、LM Studio、vLLM，带每日上限与美元预算

## 适用场景

- 持续盘点组织暴露的子域名、端口、服务与证书
- 新 CVE 出现时确认自家主机是否在受影响范围内
- 用只读复现证据替代人工逐条核验漏洞发现
- 在私有网络部署 Sentinel 检查内网资产

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L27: **Bring your own AI:** Anthropic, OpenAI or OpenRouter on your own key, or fully local with Ollama, LM Studio or vL
> L44: cvENGINE is a self-hosted external attack surface and vulnerability assessment platform. Give it your domains and i
> L11:  Self-hosted with Docker Compose

## 星数曲线

```mermaid
xychart-beta
    title "hevnsnt/CVEngine 星数(近 26 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 0 --> 896
    line [19, 359, 412, 437, 465, 531, 545, 557, 691, 703, 710, 711, 715, 719, 738, 739, 742, 743, 744, 745, 747, 748, 747, 776, 807, 817]
```

2026-10-26 19 → 2026-11-28 817（+798）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `b8ffd3ec257e` · [字段定义](../../DATASET.md)*
