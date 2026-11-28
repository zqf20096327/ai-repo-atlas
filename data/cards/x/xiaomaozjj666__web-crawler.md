# xiaomaozjj666/web-crawler

⭐ 12 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/xiaomaozjj666/web-crawler) · [官网](https://xiaomaozjj666.github.io/web-crawler/) · 个人维护 · 中文 README

**面向开发者的隐身网页采集与授权安全测试工具集**

Scrapling 风格的 Python 爬虫库，核心能力包括：基于 lxml 的自适应选择器（站点改版后可凭指纹重定位元素）、curl_cffi 重放浏览器 TLS/JA3 指纹的隐身 HTTP、Playwright JS 渲染、回调式 Spider 框架（重试、去重、robots、限速、缓存、管道）。AI 部分提供 AIExtractor 自然语言转选择器、DeepSeek 驱动的 JS 逆向 Agent、图片验证码识别与 pentest 侦察子包。默认拒绝私网目标以防 SSRF，仅限授权用途。经 PyPI 以 stealth-web-crawler 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自适应选择器：指纹保存与结构相似度重定位
- curl_cffi 重放 TLS/JA3 指纹，缺失时降级 httpx
- JS 逆向 Agent：观察-思考-行动循环 + MCP/Web UI/CLI 三入口
- 默认 SSRF 防护：拒绝私网/环回/云元数据目标

## 适用场景

- 对已授权目标做反爬环境下的数据采集与字段提取
- 逆向研究目标站点的前端加密与签名逻辑
- 对自有资产做端口/路径/子域等授权渗透侦察

## 场景标签

`网页抓取` `网络安全` · 领域:效率与自动化

## 证据(README 行号)

> L12: Scrapling 风格的隐身网页爬虫库：**自适应选择器**、**TLS 指纹隐身 HTTP**、**JS 渲染**与**回调式 Spider 框架**，另附一套应用层资源下载器与本地 Web UI。
> L82: - **JS 逆向 Agent** — `ReverseAgent` 通过 **观察 → 思考 → 行动** 循环（`CamoufoxFetcher` + DeepSeek-V4.1-Flash）逆向目标站点的加密逻辑：注入 JS
> L102: 本库是**面向开发者的隐身网页采集与安全研究工具集**，把两套能力放在同一个包里，方便做端到端的研究与自动化：

## 星数曲线

```mermaid
xychart-beta
    title "xiaomaozjj666/web-crawler 星数(近 3 点)"
    x-axis ["2026-11-18", "2026-11-23", "2026-11-28"]
    y-axis "stars" 10 --> 13
    line [11, 12, 12]
```

2026-11-18 11 → 2026-11-28 12（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 mid · 依据 README sha `7aaaf15d558a` · [字段定义](../../DATASET.md)*
