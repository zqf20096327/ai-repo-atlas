# HeyiCAo/explain-this-ai

⭐ 14 · JavaScript · 推送 2026-07-06 · [GitHub](https://github.com/HeyiCAo/explain-this-ai) · [官网](https://chromewebstore.google.com/detail/explain-this-smooth-ai-in/dpibmfnhicbhmggmihhnlmbbmhpgabda?authuser=0&hl=en) · 个人维护 · 中文 README

**网页划词即时 AI 解释的 Chrome 扩展**

面向网页阅读者的 Chrome 扩展：选中文字后点击 Explain this 或按快捷键，获得流式的中英文解释（简短三句或详细带示例）。默认内置免费模式每日 50 次、无需 API key，由部署在 Cloudflare Workers 上的后端持有凭据并实施限流（每日 50 次、每分钟限速、千字符上限）。隐私设计上按需授权站点访问、可选本地历史；进阶用户可 BYOK（OpenAI/Gemini/DeepSeek）直连供应商。以 npm 构建、Chrome 加载未打包扩展方式开发安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 划词后流式生成中英文解释，无需 API key 每日 50 次免费
- Cloudflare Workers 后端持有凭据并实施每日/每分钟限流与千字符上限
- 隐私控制：按需站点授权、可禁用并清除本地历史与缓存
- BYOK 支持 OpenAI/Gemini/DeepSeek，密钥存 chrome.storage 直连供应商

## 适用场景

- 阅读外文网页时划词即时获取解释
- 不配置 API key 直接使用免费 AI 解释额度
- 控制扩展可访问的站点范围与本地历史记录

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L8: friction. Highlight a word, phrase, or passage, click **Explain this**, and get a
> L53: Chrome extension → Explain This backend → AI provider

## 星数曲线

```mermaid
xychart-beta
    title "HeyiCAo/explain-this-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `771fcdc5f014` · [字段定义](../../DATASET.md)*
