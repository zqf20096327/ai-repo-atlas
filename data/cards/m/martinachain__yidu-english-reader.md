# martinachain/yidu-english-reader

⭐ 34 · TypeScript · MIT · 推送 2026-09-15 · [GitHub](https://github.com/martinachain/yidu-english-reader) · 个人维护 · 中文 README

**面向中文学习者的英文阅读器：AI 查词拆句 + 间隔重复复习**

易读是一个产品两个入口的英文阅读工具：Next.js 网页阅读器（导入 EPUB/PDF/Markdown）与 Chrome 浏览器插件（任意网页划词划句）。双击查词、划选拆句由浏览器 fetch 直连 DeepSeek 官方接口（deepseek-chat）完成，无服务端代理；查过的词句自动入生词本与句子库，按 1/3/7/14/30/60 天阶梯做间隔重复复习。全部数据存浏览器 IndexedDB，无账号无服务器数据库，换设备不同步；插件离线查词用本地词典，插件同步域名写死在 manifest.json，自有部署需改配置重打包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双击查词、划选拆句调用 DeepSeek，浏览器直连无服务端代理
- 网页阅读器与浏览器插件共享生词本、句子库与 SRS 复习队列
- 数据全存浏览器 IndexedDB，key 只存本地 localStorage/chrome.storage
- 支持导入 EPUB/PDF/Markdown，PDF 懒加载分页

## 适用场景

- 读英文原版书时即点即查生词并自动进复习计划
- 刷英文网页随手划词划句，收藏汇总到同一生词本
- 自部署纯前端静态站点，用各自的 DeepSeek key 使用

## 场景标签

 · 领域:语言学习/阅读工具

## 证据(README 行号)

> L9: **易读**是一个面向中文学习者的英文阅读工具，一个产品、两个入口：
> L21: - **双击查词** —— 双击任意单词，AI 结合上下文给出本句中的中文释义
> L22: - **划选拆句** —— 选中一个长句，AI 拆出句子结构、关键短语、难点注解和完整翻译

## 星数曲线

```mermaid
xychart-beta
    title "martinachain/yidu-english-reader 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-27 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `38eb03da3b7a` · [字段定义](../../DATASET.md)*
