# mage-os/module-automatic-translation

⭐ 33 · PHP · MIT · 推送 2026-10-16 · [GitHub](https://github.com/mage-os/module-automatic-translation) · 组织维护

**Magento 商店的 AI 内容自动翻译模块（产品/分类/CMS 页面）**

MageOS 的 Magento 2 扩展，通过 AI 翻译引擎自动翻译产品、分类、CMS 页面与静态块内容。默认集成 DeepL、OpenAI 和 Google Gemini 三种引擎，可通过实现 TranslatorInterface 扩展其他引擎。产品翻译支持 cron 定时任务与后台手动按钮两种方式，分类、页面与静态块仅支持手动翻译；模块自动创建 'skip translation' 与 'last translation date' 属性标记已翻译产品，支持按天数配置的周期性自动重译。注意：页面与静态块翻译会覆盖原内容，建议先使用 'Save & Duplicate' 复制。通过 Composer 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 默认集成 DeepL / OpenAI / Google Gemini 三种翻译引擎，可扩展
- 产品翻译支持 cron 定时任务与后台手动按钮
- 基于 'skip translation' 与 'last translation date' 属性的重译标记机制
- 按 store view 维度的启用/源语言/目标语言配置

## 适用场景

- 多语言 Magento 商店批量翻译产品内容
- 定期自动重译内容有更新的产品
- 翻译分类、CMS 页面与静态块以覆盖新语言市场

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L5: The **MageOS Automatic Translation** module allows you to automatically translate content in your Magento store, suc
> L61: - **DeepL**, **OpenAI** and **Google Gemini** are the supported engines by default. You can easily extend the modul

## 星数曲线

```mermaid
xychart-beta
    title "mage-os/module-automatic-translation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-26 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `7b1cf0438fe2` · [字段定义](../../DATASET.md)*
