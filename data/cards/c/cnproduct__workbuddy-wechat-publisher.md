# cnproduct/workbuddy-wechat-publisher

⭐ 82 · TypeScript · 推送 2026-03-29 · [GitHub](https://github.com/cnproduct/workbuddy-wechat-publisher) · 组织维护 · 中文 README

**微信公众号内容生产技能包：写作→配图→排版→发布草稿箱**

面向公众号运营者的自动化技能包，由 SKILL.md 工作流编排与四个子技能组成：内容撰写（输出带配图占位符的 Markdown）、配图生成（调用 DALL-E/Midjourney 等 API 或从 Unsplash/Pexels 图库匹配）、HTML 排版（多主题配色，输出可粘贴微信编辑器的 HTML）、草稿箱发布（调用微信公众号 API 返回草稿 ID 与预览链接）。使用前需在微信公众平台获取 AppID/AppSecret、配置 IP 白名单并开通草稿箱权限（需微信认证）。Python 脚本依赖 requests。

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

- 四个子技能串联：写作→配图→排版→草稿箱发布
- 支持完整工作流与单独调用子技能两种方式
- HTML 排版提供科技蓝/活力橙/清新绿等多主题配色
- 配图支持生图 API 与免费图库匹配两种方式

## 适用场景

- 只给主题就自动产出图文并茂的公众号文章并发布到草稿箱
- 批量生成符合公众号风格的文章草稿
- 将 Markdown 自动转换为微信公众号排版 HTML

## 场景标签

`工作流自动化` `AI 写作` `图像生成` · 领域:效率与自动化

## 证据(README 行号)

> L7: 当用户给出文章主题或指令时，自动执行"写作 -> 配图 -> 排版 -> 发布"的全流程，最终产出图文并茂、排版美观的公众号文章。
> L46: **功能**：调用微信公众号API，发布文章到草稿箱

## 星数曲线

```mermaid
xychart-beta
    title "cnproduct/workbuddy-wechat-publisher 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 81 --> 83
    line [82, 82]
```

2026-10-18 82 → 2026-10-31 82（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `f6aafd7ac8e6` · [字段定义](../../DATASET.md)*
