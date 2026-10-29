# aiguozhi123456/juso-search

⭐ 30 · TypeScript · MPL-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/aiguozhi123456/juso-search) · [官网](https://aiguozhi123456.github.io/juso-search/) · 个人维护 · 中文 README

**面向人类与本地 AI 智能体的双面搜索聚合浏览器扩展**

基于 Manifest V3/WXT 的 Chromium 开源扩展（双面搜/Juso）：人类用户可在统一入口选择、切换传统搜索引擎（Google、Bing、Baidu、抖音、小红书、哔哩哔哩、Yandex、DuckDuckGo）、站外搜索、自定义引擎、AI 对话站点与已配置的 AI 搜索 API（Tavily、Exa、Brave、Stepfun、Jina、Doubao）；本地 AI 智能体经 Agent Bridge（CLI Skill 或 MCP Server）以 5 个受限 action 调用同一浏览器，密钥存于 chrome.storage.local 仅 worker 读取、不离开扩展。聚合指统一接入与切换，不表示默认并行请求或结果融合。安装途径为 Chrome Web Store、GitHub Release 加载解压包或源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五类搜索来源（传统引擎/站外搜索/自定义引擎/AI 搜索 API/AI 对话站点）统一选择与快切
- 本地智能体经 Agent Bridge 以 CLI Skill 或 MCP Server 两种方式接入（5 个受限 action）
- AI 搜索服务密钥仅由扩展后台 service worker 本地管理，不交给 UI 或智能体
- SERP 结果页注入快切栏、划词就近搜索、AI 搜索结果本地缓存

## 适用场景

- 在一个入口聚合切换多个传统与 AI 搜索来源
- 为本地 AI 智能体提供不暴露密钥的受限搜索能力
- 把 AI 对话站点或任意带 %s 的网址当作搜索引擎使用

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L16: Juso 是一个开源的双面搜索产品：它让人类用户在同一入口选择、切换传统搜索引擎、站外搜索（Site Engine）、自定义引擎、AI 对话引擎与已配置的 AI 搜索服务；也让本地 AI 智能体通过同一台浏览器调用 AI 搜索 A
> L103: 智能体接入有 **CLI Skill** 与 **MCP Server** 两种方式，二选一即可。两者走同一个 Agent Bridge、同样的 5 个 action，密钥同样不离开扩展。
> L133: 无论哪种方式，本地智能体都可列出已配置的服务、以**显式**服务参数进行 API 搜索、按实例搜索支持实例的服务，或通过浏览器检索受支持的传统搜索引擎（Google、Bing、Baidu、Yandex、DuckDuckGo、哔哩

## 星数曲线

```mermaid
xychart-beta
    title "aiguozhi123456/juso-search 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-29 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d98632b0b236` · [字段定义](../../DATASET.md)*
