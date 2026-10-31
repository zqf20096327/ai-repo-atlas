# KuiChi-x/reverseloom

⭐ 31 · Python · Apache-2.0 · 推送 2026-09-23 · [GitHub](https://github.com/KuiChi-x/reverseloom) · 个人维护 · 中文 README

**把浏览器交给 LLM 的网页逆向 Agent：自动还原签名并生成无浏览器爬虫**

基于 graphloom 框架构建的 AI 浏览器 Agent：驱动 Chromium 系浏览器（patchright），通过 CDP 断点、网络捕获与 JS 调试器向模型暴露完整上下文，逆向签名/加密参数后在 Node+jsdom 沙箱中复现生成器，最终产出脱离浏览器、可冷启动的纯代码爬虫或 API 客户端。面向爬虫开发与网页逆向人员，支持 30+ 工具、自定义技能、人工介入登录/验证码；声明仅限研究、测试与授权数据集成。模型需支持图像输入与流式输出，需本机已装 Chromium 系浏览器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- observer 覆写注入：每轮仅注入当前快照，长会话不撑爆上下文
- CDP 断点/网络/脚本调试工具链 + Node 沙箱复现签名/加密生成器
- 产出无浏览器、可冷启动的独立 Python 爬虫
- 30+ 工具、自定义技能、人工交互接续（登录/验证码/澄清）

## 适用场景

- 逆向带签名/加密参数的网站接口并生成可长期运行的爬虫
- 在 Akamai 等反爬环境下采集授权目标站点的数据
- 让 Agent 跨多个网站完成自动化浏览与信息汇总任务

## 场景标签

`浏览器自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L5: ### 🕸️ Hand the whole browser to an LLM — it gets in, reverses the protocol, and writes a crawler that runs without 
> L35: |🧱 **Wall 2**|**Can't reverse it** — data is signed / tokenized / encrypted|hand-reading obfuscated JS, a full day 

## 星数曲线

```mermaid
xychart-beta
    title "KuiChi-x/reverseloom 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-31 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `0cc233ef533a` · [字段定义](../../DATASET.md)*
